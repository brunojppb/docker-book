## Docker Book - Notes

Installing docker on linux
```bash
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
```