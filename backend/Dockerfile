FROM python:3.11-slim

WORKDIR /app

RUN pip install flask

COPY app.py /app/app.py
COPY .env /app/.env

CMD ["python", "app.py"]