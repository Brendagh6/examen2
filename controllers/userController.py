from models.user import User
from config import db


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def create_user(username, password):
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user
