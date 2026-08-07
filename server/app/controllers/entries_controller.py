from app.extensions import db
from app.models.entries import Entry
from app.utils import paginate


## CRUD OPERATIONS
class EntryController:

# Add a new entry to the database
    @classmethod
    def create_entry(cls, data):
        payload = dict(data)
        for field in ['title', 'entry', 'journal_id']:
            if field not in payload:
                return None
        entry = Entry(title=payload['title'], entry=payload['entry'], journal_id=payload['journal_id'])
        db.session.add(entry)
        db.session.commit()
        return entry

    @classmethod
    def get_all_entries(cls):
        query = Entry.query
        return paginate(query=query)

# Get a specific entry by ID from the database
    @classmethod
    def get_entry_by_id(cls, entry_id):
        return Entry.query.get(entry_id)

    @classmethod
    def update_entry(cls, entry_id, data):
        entry = Entry.query.get(entry_id)
        if not entry:
            return None
        payload = dict(data)
        if 'title' in payload and payload['title']:
            entry.title = payload['title']
        if 'entry' in payload and payload['entry']:
            entry.entry = payload['entry']
        if 'journal_id' in payload and payload['journal_id']:
            entry.journal_id = payload['journal_id']
        db.session.commit()
        return entry

# Delete a specific entry by ID from the database
    @classmethod
    def delete_entry(cls, entry_id):
        entry = Entry.query.get(entry_id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
            return True
        return None