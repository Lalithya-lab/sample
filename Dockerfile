# Use an official Python image as a base
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
