FROM python:3-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install -e /app/videos
EXPOSE 8000
CMD gunicorn --paste /app/videos/development.ini -b :8000