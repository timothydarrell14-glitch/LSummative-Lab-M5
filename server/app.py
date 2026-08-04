from flask import Flask
from flask_migrate import Migrate

from extensions import db, ma, jwt
from models import Entry, Journal, User

app = Flask(__name__)

#-------------------------PAGINATE-----------------------------------#

def paginate(query, page, per_page):
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

#--------------------------ROUTEs-----------------------------------#



#--------------------------RUN--------------------------------#

if __name__ == "__main__":
    app.run(port=5555, debug=True)