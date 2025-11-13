# Dockerfile
# This file defines how to build the Earthquake app

# Start from a lightweight Python 3.9 image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first for better caching
COPY requirements.txt .

# Install your Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now, copy the rest of your project code (app.py, etc.)
COPY . .

# Expose the port that Streamlit runs on
EXPOSE 8501

# The command to run your app when the container starts
CMD ["streamlit", "run", "app.py"]
