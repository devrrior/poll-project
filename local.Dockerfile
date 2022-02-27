FROM python:3.9.10-alpine3.15
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.local" ]
