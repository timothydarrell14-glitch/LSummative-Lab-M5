from extensions import ma
from models.journals import Journal

class JournalSchema(ma.SQLAlchemyAutoSchema):
    model = Journal
    load_instance = True

journal_schema = JournalSchema()
journals_schema = JournalSchema(many=True)

