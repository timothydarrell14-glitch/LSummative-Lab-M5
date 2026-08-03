from flask import Flask
from flask_migrate import Migrate

from extensions import db, ma, jwt

app = Flask(__name__)

#-------------------------CONFIGs------------------------------------#

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///journals.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = 'jwt_secret_key'

db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

migrate = Migrate(db, app)

#--------------------------ROUTEs-----------------------------------#

if __name__ == "__main__":
    app.run(port=5555, debug=True)