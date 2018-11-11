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
```


