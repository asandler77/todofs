# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container to the root directory
WORKDIR /

# Copy the dependency files to the root directory
COPY pyproject.toml poetry.lock /

# Install dependencies
RUN pip install poetry && poetry install --no-dev

# Install curl
RUN apt-get update && apt-get install -y curl && apt-get clean

# Copy the rest of the application code to the root directory
COPY . /

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["poetry", "run", "python", "main.py"]
