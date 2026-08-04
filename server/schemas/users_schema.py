from extensions import ma
from marshmallow import fields

from models.users import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        unknown = 'exclude'

    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)