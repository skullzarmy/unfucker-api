# Use the official Python image from the Docker Hub
FROM python:3.9

# Install git and libmagic (required for python-magic)
RUN apt-get update && apt-get install -y \
    git \
    libmagic1

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set environment variables needed for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 3825 for the app to listen on
EXPOSE 3825

# Run the command to start the app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:3825", "--workers", "3"]
