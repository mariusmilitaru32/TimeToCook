from flask import flash, redirect, render_template, request, session, url_for
from timetocook import app, db
from timetocook.models import Recipe, UserFavorite, User, RecipeCategory
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
@app.route("/index")
def index():
    rated_recipes = list(Recipe.query.filter(Recipe.rating >= 4).all())
    return render_template("index.html", rated_recipes=rated_recipes)
