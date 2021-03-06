## Multi-container application stack

- node.js Express app
- redis primary container to hold a redis cluster
- two redis replica containers to represent the cluster state
- logging container to collect app logs

### Starting off out node.js app

```sh
mkdir -p nodejs/nodeapp
cd nodejs/nodeapp
wget https://raw.githubusercontent.com/jamtur01/dockerbook-code/master/code/6/node/nodejs/nodeapp/package.json
wget https://raw.githubusercontent.com/jamtur01/dockerbook-code/master/code/6/node/nodejs/nodeapp/server.js
cd ..
touch Dockerfile
```

Now lets make our node.js image
```dockerfile
FROM ubuntu:16.04
LABEL maintainer="bruno@example.com"
ENV REFRESHED_AT 2018-12-02

RUN apt-get -yqq update
RUN apt-get -yqq install curl build-essential
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get install -y nodejs

# check node version
RUN echo $(nodejs -v)
# Create logs folder
RUN mkdir -p /var/log/nodeapp
# Add our local nodeapp folder to opt
ADD nodeapp /opt/nodeapp/
# use opt path as our working directory
WORKDIR /opt/nodeapp/
# install app dependencies
RUN npm install
# map the logs folder to a persistent volume in the host machine
VOLUME [ "/var/log/nodeapp" ]
# expose express app port
EXPOSE 3000
# fire-up node app
ENTRYPOINT [ "nodejs", "server.js" ]
```

Lets build our node.js app image
```sh
docker build -t bruno/nodejs .
```

### Building our redis cluster

Lets build our redis base image
```dockerfile
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
# we don't issue any commands here. we are just bunding on top of this image
CMD []
```

Lets go ahead and build our redis image
```dockerfile
docker build -t bruno/redis_base .
```

Now, lets declare our primary redis image
```dockerfile
FROM bruno/redis_base
LABEL maintainer="bruno@example.com"
ENV REFRESHED_AT 2018-12-01
# Fire up redis server and point log files to volume declared in base image
ENTRYPOINT 	[ "redis-server", "--protected-mode no", "--logfile /var/log/redis/redis-server.log" ]
```

Lets build it now:
```sh
docker build -t bruno/redis_primary .
```

#### Building our redis replica

Lets declare a redis replica to serve as a redundant redis instance to our nodejs app
```dockerfile
# base our image on our redis base
FROM bruno/redis_base
LABEL maintainer="bruno@example.com"
ENV REFRESHED_AT 2018-12-01

# fire up redis server and make it slave of the primary redis instance
# also point logs to same persistent volume declared in base image
ENTRYPOINT [ "redis-server", "--protected-mode no", "--logfile /var/log/redis/redis-replica.log", "--slaveof redis_primary 6379" ]
```

## Running our cluster in a docker network

Lets create a specific network for our app
```sh
# create a network called express
docker network create express
```

Now lets run the redis primary container on the previously created network
```sh
# -d = run it in background
# -h = Sets the hostname of the container
# --net = specify docker network
docker run -d -h redis_primary --net express --name redis_primary bruno/redis_primary
```

Lets check the logs from our redis container
```sh
docker logs redis_primary
```
You will see nothing. The reason behind this is that redis is logging into a file we specified in the image instead of the default output.  
Lets create a temporary container and `cat` the log file
```sh
docker run -ti --rm --volumes-from redis_primary ubuntu cat /var/log/redis/redis-server.log
```
Here we can see that out redis server is running as expected.


Lets fire up our redis replica
```sh
docker run -d -h redis_replica1 --name redis_replica1 --net express bruno/redis_replica
```

Now lets check the container logs
```sh
docker run -ti --rm --volumes-from redis_replica1 ubuntu cat /var/log/redis/redis-replica.log
```
Now we can see that our redis replica is connected to the master redis and the sync works!


Lets add a second replica
```sh
docker run -d -h redis_replica2 --name redis_replica2 --net express bruno/redis_replica
```

### Creating our nodejs container
Lets create our nodejs app container
```sh
docker run -d -p 3000:3000 --name nodeapp --net express bruno/nodejs
```