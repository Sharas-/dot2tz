from python:3.8.5-alpine
run apk update && apk add --no-cache geos
workdir /srv
copy requirements.txt .
run pip install -r requirements.txt
copy code/ .
env GUNICORN_CMD_ARGS --bind=0.0.0.0:80 --workers=2 --worker-class=sync
entrypoint ["gunicorn", "webapp:app"]
