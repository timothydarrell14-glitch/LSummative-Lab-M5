from extensions import db
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String, nullable=False)

    @validates('email')
    def validate_email(self, email):
        if not isinstance(email, str):
            raise ValueError
        email = email.strip().lower()
        if '@' not in email or '.com' not in email:
            raise ValueError
        return email

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(password)
