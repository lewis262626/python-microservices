FROM python:3.7.5-alpine

WORKDIR /usr/src/app

RUN apk add build-base

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP main.py

CMD ["flask", "run", "--host=0.0.0.0"]
