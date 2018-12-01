FROM ubuntu:16.04
LABEL maintainer="bruno@example.com"
ENV REFRESHED_AT 2018-12-01

RUN apt-get -yqq update
RUN apt-get install -yqq software-properties-common python-software-properties
# add redis repo to grap latest redis version instead of old shipped with Ubuntu
RUN add-apt-repository ppa:chris-lea/redis-server
RUN apt-get -yqq update
# install redis
RUN apt-get install redis-server redis-tools

VOLUME [ "/var/lib/redis", "/var/log/redis" ]
# expose redis port
EXPOSE 6379
CMD []