# Komplano

## Use cases

- Chores planner (MVP)
- Shopping list
- Budget tracking
- Calendar
- Notes(?)

## Technology stack

### API

- FastAPI
- PostgreSQL
- SQLAlchemy/psycopg/Alembic?

### Client

 - Angular?

## Development

### Requirements

- Docker
- [Pipenv](https://pipenv.pypa.io/en/latest/basics/#example-pipfile-pipfile-lock)

### Setup

```bash
# create .env file (e.g., by renaming .env.sample)

# Start the database
docker-compose up -d
OR docker compose up -d

# Install dependencies
pipenv install

# Swith to pipenv shell
pipenv shell

# Start app
univorn app.main:app --reload
```