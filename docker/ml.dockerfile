# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY recom_model.py recom_model.py
COPY pack_pkl.py pack_pkl.py

ENV DATA=https://raw.githubusercontent.com/XinyuTian1104/CompSci401/main/data/ds2.csv
ENV VERSION=2

CMD ["python3", "pack_pkl.py"]
