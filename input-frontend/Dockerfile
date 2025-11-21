FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY templates ./templates

RUN pip install flask redis

EXPOSE 5000

CMD ["python", "app.py"]
