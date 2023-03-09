FROM python:3.8
LABEL maintainer="simonz@uoregon.edu"
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install requests
RUN pip install -r requirements.txt

