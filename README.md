# Docker Book - Notes

Installing docker on linux
```sh
# install dependencies
$ apt-get install apt-transport-https ca-certificates curl software-properties-common

# add official Docker GPC key
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# add Docker APT repo
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# update apt sources
$ sudo apt-get update

# install docker engine
$ sudo apt-get install docker-ce

# test docker installation
$ sudo docker info
```

If using UFW (Uncomplicated Firewall) on Ubuntu, we should enable `forwarding packets`.
Update `DEFAULT_FORWARD_POLICY` on `/etc/default/ufw` file.

```sh
DEFAULT_FORWARD_POLICY="ACCEPT"
```

Save and reload UFW.
```sh
$ sudo ufw reload
```
## Docker service commands

```sh
# Check status
$ sudo service docker status

# Stop Docker 
$ sudo service docker stop

# Start Docker
$ sudo service docker start

# upgrade docker
$ sudo apt-get update
$ sudo apt-get install docker-engine
```

## Running first command

```sh
# -i = leave STDIN open for container
# -t = attach pseudo-tty to container and let us issue commands
# ubuntu = which image to use when creating the container. Ubuntu is a base image provided by docker
# /bin/bash = run the bash command inside container
$ sudo docker run -i -t ubuntu /bin/bash

# Now we can play with a fully fledged ubuntu container 
#Type exit to go back to host OS
```

## More commands
```sh
# list containers
# -a = all containers
$ docker ps -a
# to only list running containers
$ docker ps

# Create a container with specific name
$ docker run --name my_awesome_container -i -t ubuntu /bin/bash

# Remove specific container
$ docker rm my_awesome_container

# Start specific container by name
$ docker start my_awesome_container

# To issue commands
$ docker attach my_awesome_container
```

## Deamon Containers

This command will start a ubuntu container and will execute this while loop until the container is stopped. 
```sh
# -d = detach container to the background
docker run \
       --name daemon_bruno \
       -d ubuntu \
       /bin/sh -c "while true; do echo hello world; sleep 1; done"
```

To check if the container is running the `while`argument:
```sh
# return the last few logs and exit
$ docker logs daemon_bruno

# To tail the logs, use the -f flag
$ docker logs -f daemon_bruno

# To get the last 10 lines of logs
$ docker logs --tail 10 daemon_bruno

# To tail without reading any previus logs
$ docker logs --tail 0 -f daemon_bruno

# To enhance the logs with timestamps
$ docker logs --tail 0 -ft daemon_bruno
```

## Inspect Container

To inspect the processes running inside the container
```sh
$ docker top daemon_bruno
```

To check statistics of a running container
```sh
# optionally, we can also pass more container names or IDs and get a live view of their stats. Here we should see CPU, MEM, Network and etc...
$ docker stats daemon_bruno <more_container_names_here>
```

## Running a process in a running container

Lets create a file in a running container issuing a command to run in background using the command `exec` and the `-d` flag.
```sh
$ docker exec -d daemon_bruno touch /etc/my_new_file
```

We can also run an interactive command like this:
```sh
docker exec -t -i daemon_bruno /bin/bash
# That will make the console available for issuing commands
```











