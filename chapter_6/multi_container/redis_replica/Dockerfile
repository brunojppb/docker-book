# base our image on our redis base
FROM bruno/redis_base
LABEL maintainer="bruno@example.com"
ENV REFRESHED_AT 2018-12-01

# fire up redis server and make it slave of the primary redis instance
# also point logs to same persistent volume declared in base image
ENTRYPOINT [ "redis-server", "--protected-mode no", "--logfile / var/log/redis/redis-replica.log", "--slaveof redis_primary 6379" ]