# Version: 0.0.1
FROM ubuntu:16.04
LABEL maintainer="bruno@example.com"
RUN apt-get update; apt-get install -y nginx
RUN echo 'Hi there, I am a web server container' \
  >/var/www/html/index.html
EXPOSE 80