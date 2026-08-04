from extensions import db
from models.entries import Entry
from app import paginate


## CRUD OPERATIONS
class EntryController:

# Add a new entry to the database
    @classmethod
    def create_entry(cls, data):
        payload = dict(data)
        for field in ['title', 'entry', 'journal_id']:
            if field not in payload:
                return None
            new_entry = Entry(**payload)
            db.session.add(new_entry)
            db.session.commit()
            return new_entry
# Get all entries from the database
    @classmethod
    def get_all_entries(cls, current_user):
        query = Entry.query.filter_by(user_id=current_user)
        return paginate(query=query)

# Get a specific entry by ID from the database
    @classmethod
    def get_entry(cls, entry_id):
        entry = Entry.query.filter_by(id=entry_id).first()
        if entry:
            return entry

# Update a specific entry by ID in the database
    @classmethod
    def update_entry(cls, entry_id, data):
        entry = EntryController.get_entry(entry_id)
        payload = dict(data)
        if not isinstance(payload, dict):
            raise ValueError
        if hasattr(payload, 'title'):
            entry.title = payload.title
        if hasattr(payload, 'entry'):
            entry.entry = payload.entry
        if hasattr(payload, 'journal_id'):
            entry.journal_id = payload.journal_id
        db.session.commit()
        return entry

# Delete a specific entry by ID from the database
    @classmethod
    def delete_entry(cls, entry_id):
        query = Entry.query.filter_by(id=entry_id).first()
        if query:
            db.session.delete(query)
            db.session.commit()
            return True