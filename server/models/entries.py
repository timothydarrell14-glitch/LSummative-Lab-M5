from extensions import db
from marshmallow import EXCLUDE

class Entry(db.Model):

    __tablename__ = 'entries'

    unknown = EXCLUDE

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    entry = db.Column(db.String)
    journal_id = db.Column(db.ForeignKey('journals.id'))
    journal = db.relationship('Journal', back_populates='entries')