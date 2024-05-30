# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir rawpy pillow numpy

# Run convert_raw_to_jpeg.py when the container launches
CMD ["python", "./convert_raw_to_jpeg.py"]
