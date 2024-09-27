# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Run the tests and then the main script
CMD sh -c "python -m unittest discover -s . && python main.py"