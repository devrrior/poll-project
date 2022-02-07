FROM python:3.9.10-alpine3.15

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN apk add --no-cache gcc musl-dev postgresql-dev
RUN python -m pip install -r requirements.txt

COPY . .
