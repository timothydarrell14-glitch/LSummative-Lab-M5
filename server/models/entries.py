from extensions import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    entry = db.Column(db.String)
    journal_id = db.Column(db.ForeignKey('journal.id'))
    journal = db.relationship('journal', back_populates='entry')