from flask import flash, redirect, render_template, request, session, url_for
from timetocook import app, db
from timetocook.models import Recipe, UserFavorite, User, RecipeCategory
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
@app.route("/index")
def index():
    rated_recipes = list(Recipe.query.filter(Recipe.rating >= 4).all())
    return render_template("index.html", rated_recipes=rated_recipes)


# login function
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            if user.banned:
                flash("Your account has been dissabled. Please contact us", "error")
                return redirect(url_for("login"))
            else:
                session["user_id"] = user.id
                session["username"] = username
                session["is_admin"] = user.admin  # required to check if user is admin
                flash(f"Welcome, {username}! You have been logged in", "success")
                return redirect(url_for("index"))
        else:
            flash("Invalid username or password", "error")
    return render_template("login.html")
