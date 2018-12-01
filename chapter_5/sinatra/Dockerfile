FROM ubuntu:16.04
LABEL maintaine="brunojppb@example.com"
ENV REFRESHED_AT 2018-11-20

# Update packages and install ruby and redis dependencies for a later chapter
RUN apt-get update -yqq; apt-get -yqq install ruby ruby-dev build-essential redis-tools
# install sinatra and dependencies
RUN gem install --no-rdoc --no-ri sinatra json redis
# create directory for sinatra app
RUN mkdir -p /opt/webapp

# Expose port to map to host
EXPOSE 4567

CMD ["/opt/webapp/bin/webapp"]