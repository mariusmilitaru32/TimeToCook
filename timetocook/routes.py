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
    """
    Route for handling user login, checks the database for a matching user,
     if user is banned and verifies the password.
    """
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


@app.route("/logout")
def logout():
    """
    Logout the user by popping the user_id and username from the session.
    Show a flash message to indicate successful logout.
    Redirect the user to the index page.
    """
    session.pop("user_id", None)
    session.pop("username", None)
    flash("You have been logged out", "success")
    return redirect(url_for("index"))


@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Register new user with username, password, and email.
    If username already exists, display error message.
    Otherwise, create new user and redirect to login page.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists.", "error")
        else:
            new_user = User(
                username=username,
                password=generate_password_hash(password),
                email=email,
            )
            db.session.add(new_user)
            db.session.commit()
            flash(f"Account created for {username}", "success")
            return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/users", methods=["GET"])
def users():
    """
    Function to render all the users in users.html
    """
    nonadmin_users = list(User.query.filter_by(admin=False).all())
    return render_template("users.html", users=nonadmin_users)


@app.route("/userban/<int:user_id>", methods=["POST", "GET"])
def userban(user_id):
    """
    Function to restrict asscess to users
    """
    user = User.query.get(user_id)
    user.banned = True
    db.session.commit()
    return redirect(url_for("users"))


@app.route("/userunban/<int:user_id>", methods=["POST", "GET"])
def userunban(user_id):
    """
    Function to unrestrict access to users
    """
    user = User.query.get(user_id)
    user.banned = False
    db.session.commit()
    return redirect(url_for("users"))


@app.route("/allrecipes")
def allrecipes():
    """
    Function to render all the recipes in allrecipes.html
    """
    recipes = list(Recipe.query.order_by(Recipe.id.desc()).all())
    return render_template("allrecipes.html", recipes=recipes)


@app.route("/myrecipes")
def myrecipes():
    """
    Function to render owners recipes in myrecipes.html
    """
    if not session.get("user_id"):
        flash("You must be logged in to view your recipes.", "error")
        return redirect(url_for("login"))

    user_id = session.get("user_id")
    my_recipes = Recipe.query.filter_by(user_id=user_id).all()
    return render_template("myrecipes.html", recipes=my_recipes)


@app.route("/favourites")
def favourites():
    """
    Function to render favourites in favourites.html
    """
    if not session.get("user_id"):
        flash("You must be logged in to view your favorites.", "error")
        return redirect(url_for("login"))

    user_id = session.get("user_id")

    # Fetch the associated Recipe objects for the user's favorites.
    favourites = (
        Recipe.query.join(UserFavorite, UserFavorite.recipe_id == Recipe.id)
        .filter(UserFavorite.user_id == user_id)
        .all()
    )

    return render_template("favourites.html", favourites=favourites)


@app.route("/add_favorite/<int:recipe_id>", methods=["POST"])
def add_favorite(recipe_id):
    """
    Function to add recipe to favourites
    """
    if not session.get("user_id"):
        flash("You must be logged in to add favorites.", "error")
        return redirect(url_for("login"))

    user_id = session.get("user_id")

    # Check if the recipe is already favourited to avoid errors
    existing_favorite = UserFavorite.query.filter_by(
        user_id=user_id, recipe_id=recipe_id
    ).first()

    if existing_favorite is None:
        new_favorite = UserFavorite(user_id=user_id, recipe_id=recipe_id)
        db.session.add(new_favorite)
        db.session.commit()
        flash("Recipe added to favorites successfully!", "success")
    else:
        flash("You have already favorited this recipe.", "error")

    return redirect(url_for("favourites"))


@app.route("/remove_favorite/<int:recipe_id>", methods=["POST"])
def remove_favorite(recipe_id):
    """
    Function to remove recipe from favourites
    """
    if not session.get("user_id"):
        flash("You must be logged in to remove favorites.", "error")
        return redirect(url_for("login"))

    user_id = session.get("user_id")

    # Find the favorite to be removed
    favorite_to_remove = UserFavorite.query.filter_by(
        user_id=user_id, recipe_id=recipe_id
    ).first()

    if favorite_to_remove:
        db.session.delete(favorite_to_remove)
        db.session.commit()
        flash("Recipe removed from favorites successfully!", "success")
    else:
        flash("Recipe not found in your favorites.", "error")

    return redirect(url_for("favourites"))


@app.route("/view_recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    """
    Function to render recipe in view_recipe.html

    """
    user_id = session.get("user_id")
    recipes = Recipe.query.get_or_404(recipe_id)
    return render_template("view_recipe.html", recipe=recipes, user_id=user_id)
