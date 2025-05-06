FROM python:3.12-slim

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "wsgi:app"]


