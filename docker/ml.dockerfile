# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY recom_model.py recom_model.py

CMD [ "python3", "-m", "run"]
