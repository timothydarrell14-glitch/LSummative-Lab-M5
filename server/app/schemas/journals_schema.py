from app.extensions import ma
from app.models.journals import Journal

class JournalSchema(ma.SQLAlchemyAutoSchema):
    model = Journal
    load_instance = True

journal_schema = JournalSchema()
journals_schema = JournalSchema(many=True)

