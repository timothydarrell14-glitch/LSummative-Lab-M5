from app import app
from extensions import db
from models.users import User
from models.journals import Journal
from models.entries import Entry


def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        for i in range(1, 11):
            user = User(
                name=f'User {i}',
                email=f'user{i}@example.com',
                password='password123'
            )
            user.hash_password('password123')
            db.session.add(user)
            db.session.flush()

            for j in range(1, 3):
                journal = Journal(name=f'Journal {j} for User {i}', user_id=user.id)
                db.session.add(journal)
                db.session.flush()

                for k in range(1, 6):
                    entry = Entry(
                        title=f'Entry {k} for Journal {j}',
                        entry=f'This is entry {k} for {journal.name}.',
                        journal_id=journal.id
                    )
                    db.session.add(entry)

        db.session.commit()
        print('Seed data created successfully.')


if __name__ == '__main__':
    seed_database()
