from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token

from extensions import db, ma, jwt
from models import Entry, Journal, User
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
# Journals
# Entries


#--------------------------RUN--------------------------------#

if __name__ == "__main__":
    app.run(port=5555, debug=True)