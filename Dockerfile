FROM python:3.9-slim

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 2. Security User
RUN adduser --disabled-password --gecos "" --uid 10014 choreouser

WORKDIR /app
COPY . .

# 3. Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4. CONFIG FIX: Create the Streamlit config directory
RUN mkdir -p /home/choreouser/.streamlit

# 5. CONFIG FIX: Move the config.toml file to the right place
# (Assumes you created config.toml in your repo)
COPY config.toml /home/choreouser/.streamlit/config.toml

# 6. Permissions
RUN chown -R 10014:10014 /app /home/choreouser

USER 10014
EXPOSE 8501

# 7. Simple CMD (Config file handles the rest)
CMD ["streamlit", "run", "app.py"]
