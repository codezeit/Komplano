FROM python:3.10
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME Komplano

# Run app.py when the container launches
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--root-path", "/api"]