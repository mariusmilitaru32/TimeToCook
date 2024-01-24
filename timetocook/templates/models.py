from timetocook import db


# User model database
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    banned = db.Column(db.Boolean, default=False)
    recipes = db.relationship(
        "Recipe", backref="user", cascade="all, delete", lazy=True
    )
    favorite_recipes = db.relationship("UserFavorite", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User username={self.username}>"


class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(
        db.Integer, db.ForeignKey("recipe_categories.id", ondelete="CASCADE")
    )
    img_url = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(25), nullable=True)

    def __repr__(self):
        return (
            f"<Recipe name={self.name}, "
            f"User username={self.user.username}, "
            f"Ingredients={self.ingredients}, "
            f"Time={self.time}, "
            f"Rating={self.rating}, "
            f"Instructions={self.instructions}>"
        )


class UserFavorite(db.Model):
    __tablename__ = "user_favorite"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipe_id = db.Column(
        db.Integer, db.ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False
    )
    recipe = db.relationship(
        "Recipe", backref=db.backref("favorited_by", lazy="dynamic")
    )

    def __repr__(self):
        return f"<UserFavorite user_id={self.user_id}, recipe_id={self.recipe_id}>"
