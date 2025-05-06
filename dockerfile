FROM python:3.12-slim

# Install dependencies sistem
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Install dependensi Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file ke dalam container
COPY . /app
WORKDIR /app

# Jalankan Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080", "--app=wsgi"]
