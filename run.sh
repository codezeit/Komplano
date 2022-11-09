#! /bin/bash

# Install python packages
#pipenv install

# Enter pipenv shell
# pipenv shell

# Start up the database docker container in  background
echo "Starting up postgresql docker container"
docker compose up -d

# Start the app
echo "Starting API"
uvicorn app.main:app --reload
