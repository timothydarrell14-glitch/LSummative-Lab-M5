from extensions import db

class Journal(db.Model):

    __tablename__ = 'journals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='journals')
    entries = db.relationship('Entry', back_populates='journal')

