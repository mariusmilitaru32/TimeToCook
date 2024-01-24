from timetocook import db


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
