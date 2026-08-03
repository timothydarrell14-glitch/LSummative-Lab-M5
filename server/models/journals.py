from extensions import db

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('user', back_populates='journals')
    entry = db.relationship('entry', back_populates='journal')

