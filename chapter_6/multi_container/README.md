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

Now lets make out node.js image
```dockerfile
FROM ubuntu:16.04
LABEL maintainer="bruno@example.com"
ENV REFRESHED_AT 2018-12-01

RUN apt-get -yqq update
RUN apt-get -yqq install nodejs npm
# Backwards compatibility issues on Ubuntu
RUN ln -s /usr/bin/nodejs /usr/bin/node
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