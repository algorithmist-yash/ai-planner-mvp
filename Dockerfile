FROM python:3.10-slim

WORKDIR /app

COPY requirements.prod.txt .
RUN pip install --no-cache-dir -r requirements.prod.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000 8501
