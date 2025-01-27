FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ ./app/
COPY tests/ ./tests/

# Expose the application port
EXPOSE 5000

# Set the default command
CMD ["python", "app/app.py"]
