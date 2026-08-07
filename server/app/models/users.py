from app.extensions import db
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import EXCLUDE

class User(db.Model):

    __tablename__ = 'users'

    unknown = EXCLUDE

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    journals = db.relationship('Journal', back_populates='user')

    @validates('email')
    def validate_email(self, key, email):
        if not isinstance(email, str):
            raise ValueError('email must be a string')
        email = email.strip().lower()
        if '@' not in email or '.com' not in email:
            raise ValueError('email must contain @ and .com')
        return email

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
