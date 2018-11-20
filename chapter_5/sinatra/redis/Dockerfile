FROM ubuntu:16.04
LABEL maintainer="bruno@example.com"
ENV REFRESHED_AT 2018-11-20

# Update packages and install ruby and redis dependencies for a later chapter
RUN apt-get update -yqq; apt-get -yqq install redis-server redis-tools

# Expose port to host
EXPOSE 6379
ENTRYPOINT ["/usr/bin/redis-server"]
CMD []