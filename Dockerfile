#import from hub.docker
FROM python:3.7-alpine

#run python
ENV PYTHONUNBUFFERED 1

#install the requirements given in the file
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

#create and set working directory
RUN mkdir /app
WORKDIR /app
COPY ./app /app

#Create a user, such that it doesnt use the rootuser
RUN adduser -D user 
USER user


