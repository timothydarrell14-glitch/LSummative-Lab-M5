from extensions import ma
from models.users import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    model = User
    load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)