from extensions import db
from models.journals import Journal
from utils import paginate

## CRUD OPERATIONS
class JournalController:

# Add a new journal to the database
    @classmethod
    def add_journal(cls, data, user_id=None):
        payload = dict(data)
        if 'name' not in payload or not payload['name']:
            return None
        journal = Journal(name=payload['name'], user_id=user_id)
        db.session.add(journal)
        db.session.commit()
        return journal

# Get all journals from the database
    @classmethod
    def get_all_journals(cls):
        query = Journal.query
        return paginate(query=query)

# Get a specific journal by ID from the database
    @classmethod
    def get_journal_by_id(cls, journal_id):
        return Journal.query.get(journal_id)

# Update a specific journal by ID in the database
    @classmethod
    def update_journal(cls, journal_id, data):
        journal = Journal.query.get(journal_id)
        if not journal:
            return None
        payload = dict(data)
        if 'name' in payload and payload['name']:
            journal.name = payload['name']
        db.session.commit()
        return journal

# Delete a specific journal by ID from the database
    @classmethod
    def delete_journal(cls, journal_id):
        journal = Journal.query.get(journal_id)
        if not journal:
            return None
        db.session.delete(journal)
        db.session.commit()
        return True