import os
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
@app.route("/get_coins")
def get_coins():
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
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration successful!")
        # return redirect(url_for("profile", username=session["user"]))
        return redirect(url_for("get_coins"))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
