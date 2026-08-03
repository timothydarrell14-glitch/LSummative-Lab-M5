from models.users import User
from extensions import db
from app import paginate


## CRUD OPERATIONS
class UserController:

# Add a new user to the database
    @classmethod
    def add_user(cls, data):
        payload = dict(data)
        for field in ['username', 'email', 'password']:
            if field not in payload:
                return None
        new_user = User(**payload)
        db.session.add(new_user)
        db.session.commit()
        return new_user

# Get all users from the database
    @classmethod
    def get_all_users(cls):
        query = User.query
        return paginate(query, page=1, per_page=10)

# Get a specific user by ID from the database
    @classmethod
    def get_user_by_id(cls, user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        return user

# Update a specific user by ID in the database
    @classmethod
    def update_user(cls, user_id, data):
        user = User.query.get(user_id)
        if not user:
            return None
        payload = dict(data)
        if not isinstance(payload, dict):
            raise ValueError
        if hasattr(payload, 'username'):
            user.username = payload.username
        if hasattr(payload, 'email'):
            user.email = payload.email
        if hasattr(payload, 'password'):
            user.password = payload.password
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