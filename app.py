import os
import boto3
import botocore
from datetime import date
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args, get_page_parameter
from flask_mail import Mail, Message
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import re
if os.path.exists("env.py"):
    import env

# Create instance of Flask
app = Flask(__name__)

# Mail Settings
mail_settings = {
    "MAIL_SERVER": os.environ.get("MAIL_SERVER"),
    "MAIL_PORT": os.environ.get("MAIL_PORT"),
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": os.environ.get("MAIL_USE_SSL"),
    "MAIL_USERNAME": os.environ.get("MAIL_USERNAME"),
    "MAIL_PASSWORD": os.environ.get("MAIL_PASSWORD"),
    "SECURITY_EMAIL_SENDER": os.environ.get("SECURITY_EMAIL_SENDER")
}

# Update application settings
app.config.update(mail_settings)

# Create instance of Flask Mail
mail = Mail(app)

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

# Pagination limit set to 6 cards per page.
CARDS_PER_PAGE = 6


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


def paginate_coins(coins, per_page):
    page = int(request.args.get('page', 1))
    offset = (page - 1) * per_page
    return coins[offset: offset + per_page]


def paginate_args(coins, per_page):
    page = int(request.args.get('page', 1))
    return Pagination(page=page, per_page=per_page, total=len(coins))


def get_page_from_url(url):
    """
    Extract page number from the url.
    Uses request referrer/regex to extract the page number from the
    URL.
    Returns the page number from the url
    """
    regexp = '(?<=page=)([^&]*)(?=&)?'
    return re.findall(regexp, request.referrer)


@app.route("/")
@app.route("/get_coins", methods=["GET", "POST"])
def get_coins():
    # Check user is in session before proceeding with request
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

        pagination_coins = paginate_coins(coins, CARDS_PER_PAGE)
        pagination = paginate_args(coins, CARDS_PER_PAGE)
        return render_template("user_coins.html",
                               coins=pagination_coins,
                               pagination=pagination)

    return render_template("user_coins.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # Check if the user is currently in session
    if "user" in session:
        flash("You are already logged in!")
        return redirect(url_for("get_coins"))
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

        # Check if the new user was saved in the database
        user_in_db = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if user_in_db:
            # put the new user into 'session' cookie
            session["user"] = request.form.get("email").lower()
            session["admin"] = False
            flash("Registration successful!")
            return redirect(url_for("get_coins"))
        else:
            flash("There was a problem creating your account")
            return redirect(url_for("register"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Find the user in the database
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                session["admin"] = existing_user["admin"]
                flash("Welcome, {}".format(
                    existing_user["fname"].capitalize()))
                return redirect(url_for("get_coins"))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username/email doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    session.pop("admin")
    return redirect(url_for("get_coins"))


@app.route("/coin_list")
def coin_list():
    # Check that the user is logged in before displaying the coin list
    # If not redirect to the login page.
    if session.get('user'):
        coins = list(mongo.db.circulation.find())
        pagination_coins = paginate_coins(coins, CARDS_PER_PAGE)
        pagination = paginate_args(coins, CARDS_PER_PAGE)
        return render_template("coin_list.html",
                               coins=pagination_coins,
                               pagination=pagination)
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/wishlist")
def wishlist():
    if session.get('user'):
        # Find the current session user in the db and retrieve the
        # users ObjectId
        user_id = mongo.db.users.find_one(
            {"email": session["user"]})["_id"]

        coin_ids = []
        # Find all entries that match the current user and add to list
        for coin in mongo.db.wishlists.find({"user_id": ObjectId(user_id)}):
            coin_ids.append((coin["_id"], coin["coin_id"]))

        coins = []
        # Gather all data into one dictionary ready for rendering.
        for id, coin in coin_ids:
            # Find the coin data from the circulation collection
            coin_data = mongo.db.circulation.find_one({"_id": ObjectId(coin)})

            # Find the users entry from the wishlist collection and add
            # in the coin data.
            user_coin = mongo.db.wishlists.find_one({"_id": id})
            user_coin['coin_data'] = coin_data
            coins.append(user_coin)

        pagination_coins = paginate_coins(coins, CARDS_PER_PAGE)
        pagination = paginate_args(coins, CARDS_PER_PAGE)

        return render_template("wishlist.html",
                               wishlist_coins=pagination_coins,
                               pagination=pagination)

    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/add_wishlist/<coin_id>")
def add_wishlist(coin_id):
    if session.get('user'):
        # Find the current session user in the db and retrieve the users
        # ObjectId
        user_id = mongo.db.users.find_one(
            {"email": session["user"]})["_id"]

        wishlist_coin = {
            "user_id": ObjectId(user_id),
            "coin_id": ObjectId(coin_id)
        }

        # Add user & coin to the wishlist collection.
        mongo.db.wishlists.insert_one(wishlist_coin)
        flash("Coin added to your wish list.")

        # Extract page number from the previous URL
        # This will redirect the user back to the same page of the
        # wish list. If they came from coin_list?/page=4 they will
        # return to the same page
        page = get_page_from_url(request.referrer)

        return redirect(url_for("coin_list", page=page))
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/delete_wishlist_coin/<wishlist_coin_id>")
def delete_wishlist_coin(wishlist_coin_id):
    if session.get('user'):
        mongo.db.wishlists.remove({"_id": ObjectId(wishlist_coin_id)})
        flash("Coin Removed From Wish List")

        # Extract page number from the previous URL
        # This will redirect the user back to the same page of the
        # wish list. If they came from wishlist?/page=4 they will
        # return to the same page
        page = get_page_from_url(request.referrer)

        return redirect(url_for("wishlist", page=page))
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/add_user_coin/<coin_id>", methods=["GET", "POST"])
def add_user_coin(coin_id):
    if session.get('user'):
        if request.method == "POST":
            # Find the current session user in the db and retrieve the
            # users ObjectId
            user_id = mongo.db.users.find_one(
                {"email": session["user"]})["_id"]

            coin = {
                "user_id": ObjectId(user_id),
                "coin_id": ObjectId(coin_id),
                "date_found": request.form.get(f"date-found-{coin_id}"),
                "notes": request.form.get(f"notes-{coin_id}")
            }
            mongo.db.coins.insert_one(coin)
            flash("Coin added to your collection.")

            # Extract page number from the previous URL
            # This will redirect the user back to the same page of the
            # wish list. If they came from coin_list?/page=4 they will
            # return to the same page
            page = get_page_from_url(request.referrer)
            return redirect(url_for("coin_list", page=page))
        else:
            return redirect(url_for("coin_list"))
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/edit_user_coin/<user_coin_id>", methods=["GET", "POST"])
def edit_user_coin(user_coin_id):
    if session.get('user'):
        if request.method == "POST":
            # Retrieve the user coin to be editted.
            user_coin = mongo.db.coins.find_one(
                {"_id": ObjectId(user_coin_id)})

            # Get new data from the form
            update_data = {"$set": {
                "date_found": request.form.get(f"date-found-{user_coin_id}"),
                "notes": request.form.get(f"notes-{user_coin_id}")
            }}

            # Update entry
            mongo.db.coins.update_many(user_coin, update_data)
            flash("Entry Successfully Updated")
            return redirect(url_for("get_coins"))
        else:
            return redirect(url_for("get_coins"))
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/delete_user_coin/<user_coin_id>")
def delete_user_coin(user_coin_id):
    if session.get('user'):
        mongo.db.coins.remove({"_id": ObjectId(user_coin_id)})
        flash("Coin Deleted From Collection")
        return redirect(url_for("get_coins"))
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/add_coin", methods=["GET", "POST"])
def add_coin():
    # Check user is in session and has admin access
    if session.get('user'):
        if session.get('admin'):
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

                return render_template("add_coin.html",
                                       denominations=denominations)
            else:
                return render_template("add_coin.html",
                                       denominations=denominations)
        else:
            flash("You do not have the correct access to view this page")
            return redirect(url_for("get_coins"))
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/delete_coin/<coin_id>")
def delete_coin(coin_id):
    # Check user is in session and has admin access
    if session.get('user'):
        if session.get('admin'):
            # Search the coins collection for all users who have
            # the coin marked for deletion and create a list
            # containing all the Object ID's
            user_coin_data = list(mongo.db.coins.find(
                {"coin_id": ObjectId(coin_id)}, {"_id": 1}))

            # Extract only the value from the key:value pair
            user_coin_ids = []
            for user_coin in user_coin_data:
                user_coin_ids.append(user_coin["_id"])

            # Delete all the user coin entries
            user_result = mongo.db.coins.delete_many(
                {"_id": {"$in": user_coin_ids}})

            # Search the wishlists collection for all users who have
            # the coin marked for deletion and create a list
            # containing all the Object ID's
            user_wishlist_data = list(mongo.db.wishlists.find(
                {"coin_id": ObjectId(coin_id)}, {"_id": 1}))

            # Extract only the value from the key:value pair
            user_wishlist_ids = []
            for user_wishlist in user_wishlist_data:
                user_wishlist_ids.append(user_wishlist["_id"])

            # Delete all the wishlist coin entries
            wishlist_result = mongo.db.wishlists.delete_many(
                {"_id": {"$in": user_wishlist_ids}})

            # Delete the coin from the database
            mongo.db.circulation.delete_one({"_id": ObjectId(coin_id)})

            flash("Deleted, {} instance(s) of the coin".format(
                user_result.deleted_count+wishlist_result.deleted_count))

            return redirect(url_for("coin_list"))
        else:
            flash("You do not have the correct access to view this page")
            return redirect(url_for("get_coins"))
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/edit_coin/<coin_id>", methods=["GET", "POST"])
def edit_coin(coin_id):
    if session.get('user'):
        if session.get('admin'):
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
                mongo.db.circulation.update(
                    {"_id": ObjectId(coin_id)}, coin_data)
                flash("Coin Successfully Updated")
                return redirect(url_for("coin_list"))
            else:
                return render_template("edit_coin.html",
                                       coin=coin,
                                       denominations=denominations)
        else:
            flash("You do not have the correct access to view this page")
            return redirect(url_for("get_coins"))
    else:
        flash("Please Log In or Register to access the site")
        return redirect(url_for("login"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("query")
    coins = list(mongo.db.circulation.find({"$text": {"$search": query}}))

    pagination_coins = paginate_coins(coins, CARDS_PER_PAGE)
    pagination = paginate_args(coins, CARDS_PER_PAGE)
    return render_template("coin_list.html",
                           coins=pagination_coins,
                           pagination=pagination)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with app.app_context():
            msg = Message(subject="New Email From Coin Collector Contact Form")
            msg.sender = request.form.get("emailaddress")
            msg.recipients = [os.environ.get("MAIL_USERNAME")]
            contact_num = request.form.get("contactnumber")
            subject = request.form.get("subject")
            message = request.form.get("message")
            msg.body = (f"Email From: {msg.sender} \n"
                        f"Contact Num: {contact_num}\n"
                        f"Subject: {subject} \nMessage: {message}")
            mail.send(msg)
            flash("Message Sent Successfully!")
            return redirect(url_for("contact"))

    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
