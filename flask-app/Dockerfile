FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/python /app
COPY src/static /app/static

ENV STATIC_FOLDER=/app/static

EXPOSE 5080

CMD ["python", "main.py"]
