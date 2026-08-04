from extensions import db
from models.journals import Journal
from app import paginate

## CRUD OPERATIONS
class JournalController:

# Add a new journal to the database
    @classmethod
    def add_journal(cls, data):
        payload = dict(data)
        for field in ['name']:
            if field not in payload:
                return None
        new_journal = Journal(**payload)
        db.session.add(new_journal)
        db.session.commit()
        return new_journal

# Get all journals from the database
    @classmethod
    def get_all_journals(cls, user_id):
        query = Journal.query.filter_by(user_id)
        return paginate(query=query)

# Get a specific journal by ID from the database
    @classmethod
    def get_journal_by_id(cls, journal_id):
        journal = Journal.query.get(journal_id)
        if not journal:
            return None
        return journal

# Update a specific journal by ID in the database
    @classmethod
    def update_journal(cls, journal_id, data):
        journal = Journal.query.get(journal_id)
        if not journal:
            return None
        payload = dict(data)
        if not isinstance(payload, dict):
            raise ValueError
        if hasattr(payload, 'name'):
            journal.name = payload.name
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