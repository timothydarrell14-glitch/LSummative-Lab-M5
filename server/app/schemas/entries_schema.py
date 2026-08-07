from app.extensions import ma
from app.models.entries import Entry

class EntrySchema(ma.SQLAlchemyAutoSchema):
    model = Entry
    load_instance = True

entry_schema = EntrySchema()
entries_schema = EntrySchema(many=True)