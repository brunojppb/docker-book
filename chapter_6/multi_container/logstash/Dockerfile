FROM ubuntu:16.04
LABEL maintainer="bruno@example.com"
ENV REFRESHED_AT 2018-12-02
RUN apt-get -yqq update
RUN apt-get -yqq install wget
RUN wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
RUN echo 'deb http://packages.elasticsearch.org/logstash/1.5/debian stable main' > /etc/apt/sources.list.d/logstash.list 
RUN apt-get -yqq update
RUN apt-get -yqq install logstash default-jdk
ADD logstash.conf /etc/
WORKDIR /opt/logstash
ENTRYPOINT [ "bin/logstash" ]
CMD [ "--config=/etc/logstash.conf" ]