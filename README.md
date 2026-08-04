# LSummative-Lab-M5

This project is a Flask-based journaling API with JWT authentication. It supports user registration and login, journal management, and entry management for each journal.

## What the app does

The backend lets users:

- Register and log in to receive a JWT token
- Create, read, update, and delete users
- Create, read, update, and delete journals
- Create, read, update, and delete journal entries
- Access protected routes using a bearer token

## Tech stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow
- Flask-JWT-Extended
- SQLite

## Project structure

```text
LSummative-Lab-M5/
├── client/              # React frontend
├── server/              # Flask backend
│   ├── app.py           # Flask app and routes
│   ├── controllers/     # CRUD controller logic
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Marshmallow schemas
│   └── seed.py          # Seed script for demo data
└── README.md
```

## Getting started

From the server folder:

```bash
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the app:

```bash
python3 app.py
```

The server will start on:

```text
http://127.0.0.1:5555
```

## API routes

### Authentication

- `POST /login` – log in a user and receive a JWT token

### Users

- `POST /users` – create a user
- `GET /users` – list users (protected)
- `GET /users/<user_id>` – get one user (protected)
- `PUT /users/<user_id>` – update a user (protected)
- `DELETE /users/<user_id>` – delete a user (protected)

### Journals

- `POST /journals` – create a journal for the authenticated user (protected)
- `GET /journals` – list journals (protected)
- `GET /journals/<journal_id>` – get one journal (protected)
- `PUT /journals/<journal_id>` – update a journal (protected)
- `DELETE /journals/<journal_id>` – delete a journal (protected)

### Entries

- `POST /entries` – create an entry (protected)
- `GET /entries` – list entries (protected)
- `GET /entries/<entry_id>` – get one entry (protected)
- `PUT /entries/<entry_id>` – update an entry (protected)
- `DELETE /entries/<entry_id>` – delete an entry (protected)

## Example auth flow

1. Create a user with `POST /users`
2. Log in with `POST /login`
3. Copy the returned token
4. Send it as a bearer token in the `Authorization` header for protected routes

## Seed data

A sample dataset can be generated with:

```bash
cd server
source .venv/bin/activate
python3 seed.py
```

This creates:

- 10 users
- 20 journals (2 per user)
- 100 entries (5 per journal)

## Notes

- The app uses SQLite by default.
- JWTs are required for all protected routes except `/login`.
- The frontend in the `client/` folder consumes this API.