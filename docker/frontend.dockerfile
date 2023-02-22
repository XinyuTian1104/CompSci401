# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY app_server.py app_server.py
COPY model.pkl model.pkl
COPY recom_model.py recom_model.py

ENV FLASK_APP=app_server.py
EXPOSE 30506
CMD [ "python3", "-m" , "flask", "run", "--host", "0.0.0.0", "--port", "30506"]