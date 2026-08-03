from extensions import db

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    entries = db.Column(db.ForeignKey('entry.id'), nullable=True)
    user = db.Column(db.ForeignKey('user.id'), nullable=False)
