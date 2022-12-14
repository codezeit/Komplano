# Komplano
![Build Status](https://github.com/codezeit/Komplano/actions/workflows/-python-app.yml/badge.svg)

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
## alternatively, use
docker compose up -d

# Install dependencies
pipenv install

# Switch to pipenv shell
pipenv shell

# Start app
uvicorn app.main:app --reload
```

### Running tests

`python -m pytest app/tests --envfile .test.env`
