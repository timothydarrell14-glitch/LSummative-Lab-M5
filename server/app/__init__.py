import os

from flask import Flask, jsonify, request
from flask_migrate import Migrate
from marshmallow import Schema, fields
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

from app.extensions import db, ma, jwt
from app.controllers.users_controller import UserController
from app.controllers.entries_controller import EntryController
from app.controllers.journals_controller import JournalController

from app.schemas.entries_schema import entry_schema, entries_schema
from app.schemas.journals_schema import journal_schema, journals_schema
from app.schemas.users_schema import user_schema, users_schema


migrate = Migrate()


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)


def create_app():
    app = Flask(__name__)
    CORS(
        app,
        origins=os.getenv("FRONTEND_URL"),
        support_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") or "sqlite:///journals.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app)

    login_schema = LoginSchema()

    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to this API"}), 200

    @app.route("/me", methods=["GET"])
    @jwt_required()
    def get_user():
        user = get_jwt_identity()
        return jsonify(user), 200

    @app.route("/signup", methods=["POST"])
    def signup():
        data = request.get_json()
        new_user = UserController.add_user(data)
        if new_user:
            token = create_access_token(
                identity=str(new_user.id),
                additional_claims={
                    "name": new_user.name,
                    "id": new_user.id,
                    "email": new_user.email,
                },
            )
            return jsonify({"token": token, "user": user_schema.dump(new_user)}), 201
        return jsonify({"message": "Missing required fields"}), 400

    @app.route("/login", methods=["POST"])
    def login():
        payload = request.get_json(silent=True)
        try:
            data = login_schema.load(payload)
        except Exception:
            return jsonify({"message": "Invalid email or password"}), 400

        user = UserController.get_user_by_email(data["email"])
        if user and user.check_password(data["password"]):
            token = create_access_token(
                identity=str(user.id),
                additional_claims={
                    "name": user.name,
                    "id": user.id,
                    "email": user.email,
                },
            )
            return jsonify({"token": token, "user": user_schema.dump(user)}), 200
        return jsonify({"message": "Invalid email or password"}), 401

    @app.route("/users", methods=["GET"])
    @jwt_required()
    def get_all_users():
        users = UserController.get_all_users()
        return users_schema.jsonify(users), 200

    @app.route("/users/<int:user_id>", methods=["GET"])
    @jwt_required()
    def get_user_by_id(user_id):
        user = UserController.get_user_by_id(user_id)
        if user:
            return user_schema.jsonify(user), 200
        return jsonify({"message": "User not found"}), 404

    @app.route("/users/<int:user_id>", methods=["PUT"])
    @jwt_required()
    def update_user(user_id):
        data = request.get_json()
        updated_user = UserController.update_user(user_id, data)
        if updated_user:
            return user_schema.jsonify(updated_user), 200
        return jsonify({"message": "User not found"}), 404

    @app.route("/users/<int:user_id>", methods=["DELETE"])
    @jwt_required()
    def delete_user(user_id):
        user = UserController.delete_user(user_id)
        if user is None:
            return jsonify({"message": "User not found"}), 404
        return jsonify({"message": "User deleted successfully"}), 200

    @app.route("/journals", methods=["POST"])
    @jwt_required()
    def add_new_journal():
        data = request.get_json()
        user_id = int(get_jwt_identity())
        new_journal = JournalController.add_journal(data, user_id=user_id)
        if new_journal:
            return journal_schema.jsonify(new_journal), 201
        return jsonify({"message": "Missing required fields"}), 400

    @app.route("/journals", methods=["GET"])
    @jwt_required()
    def get_all_journals():
        journals = JournalController.get_all_journals()
        return journals_schema.jsonify(journals), 200

    @app.route("/journals/<int:journal_id>", methods=["GET"])
    @jwt_required()
    def get_journal_by_id(journal_id):
        journal = JournalController.get_journal_by_id(journal_id)
        if journal:
            return journal_schema.jsonify(journal), 200
        return jsonify({"message": "Journal not found"}), 404

    @app.route("/journals/<int:journal_id>", methods=["PUT"])
    @jwt_required()
    def update_journal(journal_id):
        data = request.get_json()
        updated_journal = JournalController.update_journal(journal_id, data)
        if updated_journal:
            return journal_schema.jsonify(updated_journal), 200
        return jsonify({"message": "Journal not found"}), 404

    @app.route("/journals/<int:journal_id>", methods=["DELETE"])
    @jwt_required()
    def delete_journal(journal_id):
        journal = JournalController.delete_journal(journal_id)
        if journal is None:
            return jsonify({"message": "Journal not found"}), 404
        return jsonify({"message": "User deleted successfully"}), 200

    @app.route("/entries", methods=["POST"])
    @jwt_required()
    def add_new_entry():
        data = request.get_json()
        new_entry = EntryController.add_entry(data)
        if new_entry:
            return entry_schema.jsonify(new_entry), 201
        return jsonify({"message": "Missing required fields"}), 400

    @app.route("/entries", methods=["GET"])
    @jwt_required()
    def get_all_entries():
        entries = EntryController.get_all_entries()
        return entries_schema.jsonify(entries), 200

    @app.route("/entries/<int:entry_id>", methods=["GET"])
    @jwt_required()
    def get_entry_by_id(entry_id):
        entry = EntryController.get_entry_by_id(entry_id)
        if entry:
            return entry_schema.jsonify(entry), 200
        return jsonify({"message": "Entry not found"}), 404

    @app.route("/entries/<int:entry_id>", methods=["PUT"])
    @jwt_required()
    def update_entry(entry_id):
        data = request.get_json()
        updated_entry = EntryController.update_entry(entry_id, data)
        if updated_entry:
            return entry_schema.jsonify(updated_entry), 200
        return jsonify({"message": "Entry not found"}), 404

    @app.route("/entries/<int:entry_id>", methods=["DELETE"])
    @jwt_required()
    def delete_entry(entry_id):
        entry = EntryController.delete_entry(entry_id)
        if entry is None:
            return jsonify({"message": "Entry not found"}), 404
        return jsonify({"message": "Entry deleted successfully"}), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(port=5555, debug=True)
