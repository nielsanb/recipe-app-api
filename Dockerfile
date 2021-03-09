#import from hub.docker
FROM python:3.7-alpine

#run python
ENV PYTHONUNBUFFERED 1

#install the requirements given in the file
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#create and set working directory
RUN mkdir /app
WORKDIR /app
COPY ./app /app

#Create a user, such that it doesnt use the rootuser
RUN adduser -D user 
USER user


