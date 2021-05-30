import os
import boto3
import botocore
from datetime import date
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import pprint
if os.path.exists("env.py"):
    import env

pp = pprint.PrettyPrinter(indent=4)

# Create instance of Flask
app = Flask(__name__)

# Configure connection to the MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Create an instance of PyMongo
mongo = PyMongo(app)

# Allowed extensions for file upload to Amazon S3
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Configure Amazon S3 Bucket for image storage
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

# Create a connection to the S3 service.
s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)


def upload_file_to_s3(file, acl="public-read"):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    try:

        s3.upload_fileobj(
            file,
            S3_BUCKET,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(S3_LOCATION, file.filename)


# CREDIT https://www.codegrepper.com/code-examples/python/validate+file+type+python+flask
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
@app.route("/get_coins", methods=["GET", "POST"])
def get_coins():
    if session.get('user'):
        # Find the current session user in the db and retrieve the
        # users ObjectId
        user_id = mongo.db.users.find_one(
            {"email": session["user"]})["_id"]

        coin_ids = []
        # Find all entries that match the current user and add to list
        for coin in mongo.db.coins.find({"user_id": ObjectId(user_id)}):
            coin_ids.append((coin["_id"], coin["coin_id"]))

        coins = []
        # Gather all data into one dictionary ready for rendering.
        for id, coin in coin_ids:
            # Find the coin data from the circulation collection
            coin_data = mongo.db.circulation.find_one({"_id": ObjectId(coin)})

            # Find the users entry from the coins collection and add
            # in the coin data. 
            user_coin = mongo.db.coins.find_one({"_id": id})
            user_coin['coin_data'] = coin_data
            coins.append(user_coin)

        pp.pprint(coins)
        return render_template("user_coins.html", coins=coins)

    return render_template("user_coins.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if email address already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Email already registered.")
            return redirect(url_for("register"))

        register = {
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "admin": False
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration successful!")
        # return redirect(url_for("profile", username=session["user"]))
        return redirect(url_for("get_coins"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            # ensure hased password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("Welcome, {}".format(
                    existing_user["fname"].capitalize()))
                # return redirect(url_for("profile", username=session["user"]))
                return redirect(url_for("get_coins"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("get_coins"))


@app.route("/coin_list")
def coin_list():

    # Check that the user is logged in before displaying the coin list
    # If not redirect to the login page.
    if session.get('user'):
        coins = list(mongo.db.circulation.find())
        return render_template("coin_list.html", coins=coins)

    return redirect(url_for("login"))


@app.route("/add_user_coin/<coin_id>")
def add_user_coin(coin_id):
    # Find the current session user in the db and retrieve the users ObjectId
    user_id = mongo.db.users.find_one(
        {"email": session["user"]})["_id"]

    coin = {
        "user_id": ObjectId(user_id),
        "coin_id": ObjectId(coin_id),
        "date_found": "date",
        "notes": "user notes"
    }
    mongo.db.coins.insert_one(coin)
    flash("Coin added to your collection.")
    return redirect(url_for("coin_list"))


@app.route("/delete_user_coin/<user_coin_id>")
def delete_user_coin(user_coin_id):
    print(user_coin_id)
    mongo.db.coins.remove({"_id": ObjectId(user_coin_id)})
    flash("Coin Deleted From Collection")
    return redirect(url_for("get_coins"))


@app.route("/add_coin", methods=["GET", "POST"])
def add_coin():
    # Request a list of denominations from Mongo for the form.
    denominations = list(mongo.db.denominations.find().sort("name", 1))

    # Check to see if the user has selected files for upload
    # Check for obverse image
    print(request.files)
    if "obverse_img_fname" not in request.files:
        file_ob_url = ""
    else:
        file_ob = request.files["obverse_img_fname"]
        if file_ob.filename == "":
            file_ob_url = ""
        else:
            if file_ob and allowed_file(file_ob.filename):
                file_ob.filename = secure_filename(file_ob.filename)
                output = upload_file_to_s3(file_ob)
                file_ob_url = str(output)

    # Check for reverse image
    if "reverse_img_fname" not in request.files:
        file_rev_url = ""
    else:
        file_rev = request.files["reverse_img_fname"]
        if file_rev.filename == "":
            file_rev_url = ""
        else:
            if file_rev and allowed_file(file_rev.filename):
                file_rev.filename = secure_filename(file_rev.filename)
                output = upload_file_to_s3(file_rev)
                file_rev_url = str(output)

    if request.method == "POST":
        coin_data = {
            "denomination": request.form.get("denomination"),
            "year": request.form.get("year"),
            "issue": request.form.get("issue"),
            "description": request.form.get("description"),
            "circulation": request.form.get("circulation"),
            "edge": request.form.get("edge"),
            "mintage": request.form.get("mintage"),
            "material": request.form.get("material"),
            "thickness": request.form.get("thickness"),
            "weight": request.form.get("weight"),
            "diameter": request.form.get("diameter"),
            "obverse_designer": request.form.get("obverse_designer"),
            "reverse_designer": request.form.get("reverse_designer"),
            "obverse_image": file_ob_url,
            "reverse_image": file_rev_url,
            "date_added": date.today().strftime("%d %b %Y"),
            "date_edited": date.today().strftime("%d %b %Y")
        }
        mongo.db.circulation.insert_one(coin_data)
        flash("Coin added to database.")

        return render_template("add_coin.html", denominations=denominations)

    return render_template("add_coin.html", denominations=denominations)


@app.route("/edit_coin/<coin_id>", methods=["GET", "POST"])
def edit_coin(coin_id):
    # Request a list of denominations from Mongo for the form.
    denominations = list(mongo.db.denominations.find().sort("name", 1))

    # Request data for the coin being edited
    coin = mongo.db.circulation.find_one({"_id": ObjectId(coin_id)})

    # Check if user has added new obverse image for upload.
    if "obverse_img_fname" in request.files:
        if request.files["obverse_img_fname"].filename == "":
            file_ob_url = coin["obverse_image"]
        else:
            file_ob = request.files["obverse_img_fname"]
            if file_ob and allowed_file(file_ob.filename):
                file_ob.filename = secure_filename(file_ob.filename)
                output = upload_file_to_s3(file_ob)
                file_ob_url = str(output)

    # Check if user has added new reverse image for upload.
    if "reverse_img_fname" in request.files:
        if request.files["reverse_img_fname"].filename == "":
            file_rev_url = coin["reverse_image"]
        else:
            file_rev = request.files["reverse_img_fname"]
            if file_rev and allowed_file(file_rev.filename):
                file_rev.filename = secure_filename(file_rev.filename)
                output = upload_file_to_s3(file_rev)
                file_rev_url = str(output)

    if request.method == "POST":
        coin_data = {
            "denomination": request.form.get("denomination"),
            "year": request.form.get("year"),
            "issue": request.form.get("issue"),
            "description": request.form.get("description"),
            "circulation": request.form.get("circulation"),
            "edge": request.form.get("edge"),
            "mintage": request.form.get("mintage"),
            "material": request.form.get("material"),
            "thickness": request.form.get("thickness"),
            "weight": request.form.get("weight"),
            "diameter": request.form.get("diameter"),
            "obverse_designer": request.form.get("obverse_designer"),
            "reverse_designer": request.form.get("reverse_designer"),
            "obverse_image": file_ob_url,
            "reverse_image": file_rev_url,
            "date_added": coin["date_added"],
            "date_edited": date.today().strftime("%d %b %Y"),
        }
        print(coin_data)
        mongo.db.circulation.update({"_id": ObjectId(coin_id)}, coin_data)
        flash("Coin Successfully Updated")
        return redirect(url_for("coin_list"))

    return render_template("edit_coin.html", coin=coin, denominations=denominations)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
