import os
from datetime import date
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Create instance of Flask
app = Flask(__name__)

# Configure connection to the MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Create an instance of PyMongo
mongo = PyMongo(app)


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
            coin_ids.append(coin["coin_id"])

        coins = []
        # Find information for each coin in the users collection from
        # the circulation collection
        for coin in coin_ids:
            coins.append(mongo.db.circulation.find_one(
                {"_id": ObjectId(coin)}))

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


@app.route("/add_coin", methods=["GET", "POST"])
def add_coin():
    denominations = list(mongo.db.denominations.find().sort("name", 1))
    print(denominations)

    if request.method == "POST":
        coin_data = {
            "denomination": request.form.get("denomination"),
            "year": request.form.get("year"),
            "issue": request.form.get("issue"),
            "description": request.form.get("description"),
            "edge": request.form.get("edge"),
            "mintage": request.form.get("mintage"),
            "material": request.form.get("material"),
            "thickness": request.form.get("thickness"),
            "weight": request.form.get("weight"),
            "diameter": request.form.get("diameter"),
            "obverse_designer": request.form.get("obverse_designer"),
            "reverse_designer": request.form.get("reverse_designer"),
            "obverse_image": request.form.get("obverse_img_fname"),
            "reverse_image": request.form.get("reverse_img_fname"),
            "date_added": date.today().strftime("%d %b %Y")
        }

        print(coin_data)

        flash("Image Uploaded")
        render_template("add_coin.html")

    return render_template("add_coin.html", denominations=denominations)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
