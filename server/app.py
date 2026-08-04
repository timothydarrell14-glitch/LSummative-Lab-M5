from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token

from controllers.users_controller import UserController
from controllers.journals_controller import JournalController
from extensions import db, ma, jwt
from models import *
from schemas import *

app = Flask(__name__)

#-------------------------PAGINATE-----------------------------------#

def paginate(query):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    paginated = query.paginate(page=page, per_page=per_page, error_out=False)
    items = paginated.items
    total = paginated.total
    return items, total

#-------------------------CONFIGs------------------------------------#

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///journals.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = 'jwt_secret_key'

db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

migrate = Migrate(app, db)

##--------------------------ROUTEs-----------------------------------##
# Login User
@app.route("/login", methods=['POST'])
def login():
    data = user_schema.load(request.get_json())
    if data:
        user = User.query.filter_by(email=data.email).first()
        if user and user.check_password(data.password):
            token = create_access_token(identity=user.id, claims={
                user.name: user.name,
                user.id: user.id,
                user.email: user.email
            })
            return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid email or password"}), 401

# Users
@app.route("/users", methods=['POST'])
def add_new_user():
    data = request.get_json()
    new_user = UserController.add_user(data)
    if new_user:
        return user_schema.jsonify(new_user), 201
    return jsonify({"message": "Missing required fields"}), 400

@app.route("/users", methods=['GET'])
def get_all_users():
    users = UserController.get_all_users()
    return users_schema.jsonify(users), 200

@app.route("/users/<int:user_id>", methods=['GET'])
def get_user_by_id(user_id):
    user = UserController.get_user_by_id(user_id)
    if user:
        return user_schema.jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

@app.route("/users/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = UserController.update_user(user_id, data)
    if updated_user:
        return user_schema.jsonify(updated_user), 200
    return jsonify({"message": "User not found"}), 404

@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    user = UserController.delete_user(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200
# Journals
@app.route("/journals", methods=['POST'])
def add_new_journal():
    data = request.get_json()
    new_journal = JournalController.add_journal(data)
    if new_journal:
        return journal_schema.jsonify(new_journal), 201
    return jsonify({"message": "Missing required fields"}), 400

@app.route("/journals", methods=['GET'])
def get_all_journals():
    journals = JournalController.get_all_journals()
    return journals_schema.jsonify(journals), 200

@app.route("/journals/<int:journal_id>", methods=['GET'])
def get_journal_by_id(journal_id):
    journal = JournalController.get_journal_by_id(journal_id)
    if journal:
        return journal_schema.jsonify(journal), 200
    return jsonify({"message": "Journal not found"}), 404

@app.route("/journals/<int:journal_id>", methods=['PUT'])
def update_journal(journal_id):
    data = request.get_json()
    updated_journal = JournalController.update_journal(journal_id, data)
    if updated_journal:
        return journal_schema.jsonify(updated_journal), 200
    return jsonify({"message": "Journal not found"}), 404

@app.route("/journals/<int:journal_id>", methods=['DELETE'])
def delete_journal(journal_id):
    journal = JournalController.delete_journal(journal_id)
    if journal is None:
        return jsonify({"message": "Journal not found"}), 404
    return jsonify({"message": "Journal deleted successfully"}), 200

# Entries


#--------------------------RUN--------------------------------#

if __name__ == "__main__":
    app.run(port=5555, debug=True)