# LSummative-Lab-M5

This project is a full-stack journaling application with a React frontend and a Flask backend. It lets users sign up, log in, and manage personal journals and journal entries with JWT-based authentication.

## Current functionality

### Frontend
The React client currently provides:

- A login form
- A sign-up form
- Persistent authentication using a JWT stored in local storage
- A simple authenticated experience that checks the current user via `/me`

### Backend
The Flask API currently supports:

- User registration with `/signup`
- User login with `/login`
- Token-based authentication for protected routes
- User lookup and profile checks via `/me`
- CRUD operations for users
- CRUD operations for journals
- CRUD operations for journal entries

## Tech stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow
- Flask-JWT-Extended
- Flask-CORS
- React
- SQLite

## Project structure

```text
LSummative-Lab-M5/
├── client/              # React frontend
│   ├── public/          # Static assets
│   └── src/             # React components and pages
├── server/              # Flask backend
│   ├── app/             # Application package
│   │   ├── controllers/ # Business logic for users, journals, entries
│   │   ├── models/      # SQLAlchemy models
│   │   ├── routes/      # Flask route definitions
│   │   └── schemas/     # Marshmallow schemas
│   ├── main.py          # Flask app entry point
│   └── seed.py          # Seed script for demo data
└── README.md
```

## Getting started

### 1. Set up the backend

```bash
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the API:

```bash
python3 main.py
```

The server will start on:

```text
http://localhost:5555
```

### 2. Set up the frontend

```bash
cd client
npm install
```

Start the React app:

```bash
npm start
```

The frontend will run on:

```text
http://localhost:4000
```

## API routes

### Authentication

- `POST /signup` – create a new user and return a JWT token
- `POST /login` – log in a user and return a JWT token
- `GET /me` – return the authenticated user from the JWT token

### Users

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

- `POST /entries` – create a journal entry (protected)
- `GET /entries` – list entries (protected)
- `GET /entries/<entry_id>` – get one entry (protected)
- `PUT /entries/<entry_id>` – update an entry (protected)
- `DELETE /entries/<entry_id>` – delete an entry (protected)

## Example auth flow

1. Open the React app and sign up or log in.
2. The app stores the returned JWT token in local storage.
3. The frontend sends that token in the `Authorization` header for protected requests.

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
- JWTs are required for protected routes.
- The frontend expects the API to be available at `http://localhost:5555` and the React app at `http://localhost:4000`.
- The client environment variable `REACT_APP_API_URL` should point to the backend URL when running the frontend.