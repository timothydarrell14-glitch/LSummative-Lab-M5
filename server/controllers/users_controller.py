from models.users import User
from extensions import db
from app import paginate


## CRUD OPERATIONS
class UserController:

# Add a new user to the database
    @classmethod
    def add_user(cls, data):
        payload = dict(data)
        for field in ['name', 'email', 'password']:
            if field not in payload:
                return None
        user = User(name=payload['name'], email=payload['email'], password=payload['password'])
        user.hash_password(payload['password'])
        db.session.add(user)
        db.session.commit()
        return user

# Get all users from the database
    @classmethod
    def get_all_users(cls):
        query = User.query
        return paginate(query=query)

# Get a specific user by ID from the database
    @classmethod
    def get_user_by_id(cls, user_id):
        return User.query.get(user_id)

# Update a specific user by ID in the database
    @classmethod
    def update_user(cls, user_id, data):
        user = User.query.get(user_id)
        if not user:
            return None
        payload = dict(data)
        if 'name' in payload and payload['name']:
            user.name = payload['name']
        if 'email' in payload and payload['email']:
            user.email = payload['email']
        if 'password' in payload and payload['password']:
            user.hash_password(payload['password'])
        db.session.commit()
        return user

# Delete a specific user by ID from the database
    @classmethod
    def delete_user(cls, user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        db.session.delete(user)
        db.session.commit()
        return True