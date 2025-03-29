from flask import Blueprint, request, jsonify
from models.user import User
from controllers.userController import get_user_by_username, create_user

user_routes = Blueprint("users", __name__)

@user_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = get_user_by_username(data["username"])
    if not user or user.password != data["password"]:
        return jsonify({"error": "Credenciales incorrectas"}), 400
    return jsonify({"message": "Inicio de sesión exitoso"})

@user_routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])