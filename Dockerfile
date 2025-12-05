# Use a lightweight Python version
FROM python:3.9-slim

# Create a user "choreouser" (ID 10014)

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid 10014 \
    "choreouser"

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Give the user permission to the folder
RUN chown -R 10014:10014 /app

# 3. SWITCH USER: Run as the safe user
USER 10014

# 4. PORT FIX: Expose Streamlit's default port
EXPOSE 8501

# 5. START COMMAND: Force Streamlit to run on 0.0.0.0 (Required for Cloud)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
