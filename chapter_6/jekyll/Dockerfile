FROM ubuntu:16.04
MAINTAINER "bruno@example.com"
ENV REFRESHED_AT 2016-06-01

RUN apt-get -yqq update
RUN apt-get install -yqq ruby ruby-dev build-essential nodejs
RUN gem install jekyll -v 2.5.3

VOLUME /data
VOLUME /var/www/html
WORKDIR /data

ENTRYPOINT [ "jekyll", "build", "--destination=/var/www/html" ]