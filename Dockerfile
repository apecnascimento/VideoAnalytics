FROM python:3-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT [ gunicorn --paste videos/development.ini -b :8000]