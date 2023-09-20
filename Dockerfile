# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# (if you have a requirements file)
# RUN pip install -r requirements.txt

# Define environment variable
ENV NAME="Python 3.9 Docker Container"

# Run your Python application
CMD ["python", "your_script.py"]