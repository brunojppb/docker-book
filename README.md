## Docker Book - Notes

Installing docker on linux
```shell
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

```shell
DEFAULT_FORWARD_POLICY="ACCEPT"
```

Save and reload UFW.
```shell
$ sudo ufw reload
```

## Docker service commands

```
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