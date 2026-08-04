from extensions import ma
from marshmallow import fields

from models.users import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    model = User
    load_instance = True
    # email = fields.Email(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)