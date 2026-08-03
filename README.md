# LSummative-Lab-M5

Backend lab project for Module 5.

## Current Functionality (Confirmed)

The app currently includes schema support for `Entry` records:

- `EntrySchema` built with `ma.SQLAlchemyAutoSchema`
- Mapped model: `Entry` (`from models.entries import Entry`)
- `load_instance = True` enabled for ORM object loading
- `entry_schema` for a single record
- `entries_schema` for multiple records (`many=True`)

Source file:

- `server/schemas/entries_schema.py`

## Project Structure

```text
LSummative-Lab-M5/
├── server/
│   ├── schemas/
│   │   └── entries_schema.py
│   └── ...
└── README.md
```

## Tech Stack

- Python
- Flask ecosystem (project structure indicates Flask-style backend)
- SQLAlchemy
- Marshmallow

## Getting Started

> Run commands from the project root on Linux.

### 1) Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

If your project has a requirements file:

```bash
pip install -r requirements.txt
```

If not, install core packages manually (adjust as needed):

```bash
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
```

### 3) Configure environment variables

Create a `.env` file (if your app uses dotenv), for example:

```env
FLASK_APP=server/app.py
FLASK_ENV=development
```

Update values to match your actual entrypoint/config.

### 4) Run the app

```bash
flask run
```

If your app uses a direct Python entrypoint instead:

```bash
python server/app.py
```

## API / Routes

Route definitions are not documented in this file yet.

Add your endpoints here once confirmed, for example:

- `GET /entries` – list entries
- `GET /entries/<id>` – get one entry
- `POST /entries` – create entry
- `PUT /entries/<id>` – update entry
- `DELETE /entries/<id>` – delete entry

## Serialization Layer

`EntrySchema` is ready for use in controllers/resources:

- Serialize one object:
  - `entry_schema.dump(entry)`
- Serialize many:
  - `entries_schema.dump(entries)`
- Deserialize payload to model instance:
  - `entry_schema.load(request_json)`

## Testing

If tests are included:

```bash
pytest
```

Or use VS Code Testing UI for discovery and execution.

## Development Notes

- Keep schemas in `server/schemas/`
- Keep models in `server/models/`
- Use schema instances (`entry_schema`, `entries_schema`) in route handlers for consistent response formatting

## License

Add your license information here.