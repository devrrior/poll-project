FROM python:3.9.10-alpine3.15
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN  apk update \
  && apk add --no-cache gcc musl-dev postgresql-dev python3-dev \
  && pip install --upgrade pip && python -m pip install -r requirements.txt 

COPY . .

RUN  python manage.py collectstatic --noinput

CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
