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


@app.route("/add_recipe", methods=["POST", "GET"])
def add_recipe():
    """
    Function for adding recipe
    """
    recipe_categories = list(RecipeCategory.query.all())
    if not session.get("user_id"):
        flash("You must be logged in to add a recipe", "error")
        return redirect(url_for("login"))
    if request.method == "POST":
        recipe = Recipe(
            name=request.form.get("recipe_name"),
            ingredients=request.form.get("recipe_ingredients"),
            time=request.form.get("recipe_time"),
            rating=request.form.get("recipe_rating"),
            instructions=request.form.get("recipe_instructions"),
            img_url=request.form.get("recipe_imgurl"),
            category_id=request.form.get("recipe_categories"),
            difficulty=request.form.get("recipe_difficulty"),
            user_id=session.get("user_id"),
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_recipe.html", recipe_categories=recipe_categories)


@app.route("/edit_recipe/<int:recipe_id>", methods=["POST", "GET"])
def edit_recipe(recipe_id):
    """
    Function to edit the recipe
    """
    recipe_categories = list(RecipeCategory.query.all())
    recipe = Recipe.query.get_or_404(recipe_id)
    if not session.get("user_id"):
        flash("You must be logged in to edit a recipe", "error")
        return redirect(url_for("login"))

    user_id = session.get("user_id")
    if recipe.user_id != user_id:  # check if the user is the owner
        flash("You must be the owner to edit the recipe.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        recipe.name = request.form.get("recipe_name")
        recipe.ingredients = request.form.get("recipe_ingredients")
        recipe.time = request.form.get("recipe_time")
        recipe.rating = request.form.get("recipe_rating")
        recipe.instructions = request.form.get("recipe_instructions")
        recipe.img_url = request.form.get("recipe_imgurl")
        recipe.category_id = request.form.get("recipe_categories")
        recipe.difficulty = request.form.get("recipe_difficulty")
        db.session.commit()
        flash("Recipe updated successfully.", "success")
        return redirect(url_for("index"))
    return render_template(
        "edit_recipe.html", recipe=recipe, recipe_categories=recipe_categories
    )


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    """
    Function to delete the recipe
    """
    recipe = Recipe.query.get_or_404(recipe_id)
    if not session.get("user_id"):
        flash("You must be logged in to delete a recipe", "error")
        return redirect(url_for("login"))

    user_id = session.get("user_id")

    if recipe.user_id != user_id:  # check if the user is the owner
        flash("You are not the owner of the recipe.", "error")
        return redirect(url_for("index"))

    # Remove the recipe from the user's favorites
    UserFavorite.query.filter_by(recipe_id=recipe_id).delete()
    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe deleted successfully.", "success")
    return redirect(url_for("index"))


@app.route("/categories")
def categories():
    """
    Function to display all categories
    """
    all_categories = RecipeCategory.query.all()
    return render_template("categories.html", categories=all_categories)


@app.route("/add_categories", methods=["POST", "GET"])
def add_categories():
    """
    Function to add categories, only the admin can add/edit/delete
    """
    if not session.get("user_id"):
        flash("You must be logged in and an admin to add categories.", "error")
        return redirect(url_for("categories"))

    user = User.query.get(session.get("user_id"))

    if not user.admin:  # check if the user is an admin
        flash("You must be an admin to add categories.", "error")
        return redirect(url_for("categories"))

    if request.method == "POST":
        category_name = request.form.get("category_name")
        if category_name:
            existing_category = RecipeCategory.query.filter_by(
                category_name=category_name
            ).first()
            if existing_category is None:
                category = RecipeCategory(category_name=category_name)
                db.session.add(category)
                db.session.commit()
                flash("Category added successfully.", "success")
                return redirect(url_for("categories"))
            else:
                flash("Category already exists.", "error")
        else:
            flash("Category name is required.")
    return render_template("add_categories.html")


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    """
    Function to delete a category, only admin can delete
    """
    if not session.get("user_id"):
        flash("You must be logged in to delete a category.", "error")
        return redirect(url_for("categories"))

    user = User.query.get(session.get("user_id"))

    if not user.admin:  # check if the user is an admin
        flash("You must be an admin to delete categories.", "error")
        return redirect(url_for("categories"))

    category_to_delete = RecipeCategory.query.get_or_404(category_id)
    db.session.delete(category_to_delete)
    db.session.commit()
    flash("Category deleted successfully.", "success")
    return redirect(url_for("categories"))


@app.route("/search", methods=["GET"])
def search():
    """
    Function to search for recipes in allrecipes.html
    """
    query = request.args.get("query")
    if not query:
        return redirect(url_for("allrecipes"))
    # Query the database for recipe names
    recipes = Recipe.query.filter(Recipe.name.ilike(f"%{query}%")).all()
    return render_template("allrecipes.html", recipes=recipes, query=query)


@app.route("/profile", methods=["POST", "GET"])
def profile():
    """
    Function to display profile page.
    Let the users to change their password
    """
    if not session.get("user_id"):
        flash("You must be logged in to view your profile.", "error")
        return redirect(url_for("login"))

    user = User.query.get(session.get("user_id"))

    if request.method == "POST":
        current_password = request.form.get("current_password")
        new_password = request.form.get("password")
        if not check_password_hash(user.password, current_password):
            flash("Incorrect current password.", "error")
            return redirect(url_for("profile"))
        user.password = generate_password_hash(new_password)
        db.session.commit()
        flash("Your password has been updated.", "success")
        session.pop("user_id")
        session.pop("username")
        return redirect(url_for("login"))

    return render_template("profile.html", user=user)


@app.errorhandler(404)
def page_not_found(e):
    """
    Function to handle 404 error
    """
    return render_template("404.html"), 404
