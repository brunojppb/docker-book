## Docker Images

A image is a `read-only` stack with whatever dependecy we need that can be used as base for our containers.

Using the `copy on write` pattern, docker can quickly read the `to be written` file from the image, make a copy of it and put it to be adited by the container. This is what makes docker so powerful.

Images are downloaded from repositories

Lets list the images available on our host:
```sh
$ docker images
```

## Where those images come from?

In our first example, our image comes from a repository called ubuntu. The image was downloaded from a repository living in a registry. The default public registry is managed by Docker, Inc. (Docker Hub). Just like Github, but as the official Docker image registry for public images.

As the Docker Hub code is open-source, we can run our own registry (e.g. Company wants to have its closed source images internally).

Each repository in the registry can have multiple images. The ubuntu repo contains many versions of the ubuntu OS.

Lets get a different Ubuntu version from the registry:
```sh
# the docker pull command will download the image to our machine
$ docker pull ubuntu:16.04
# Now lets list our images again
$ docker images
# We should see the latest ubuntu image we used in the last chapters and also the 16.04 version.
```

Now we can fire up a container with the specific image we just pulled using its `TAG` like this:
```sh
# here we specify the repository "ubuntu" and just after it comes its tag "16.04"
# That way we can specify precisely which version we want to use
docker run -t -i \
	--name container_ubuntu_16_04 \
	ubuntu:16.04 \
	/bin/bash
```

## Building custom images

To build custom images, we need a `Dockerfile` that will execute whatever commands we need to setup the image.
Here is a NGINX image example
```dockerfile
# Version: 0.0.1
# Use the ubuntu image tagged with 16.04 as base
FROM ubuntu:16.04
LABEL maintainer="bruno@example.com"
# perform updates and install nginx
RUN apt-get update; apt-get install -y nginx
# Create html file with content
RUN echo 'Hi there, I am a web server container' \
  >/var/www/html/index.html
# make port 80 available
EXPOSE 80
``` 

Now lets build the image using our `Dockerfile`:
```sh
# This command will generate a new image based on our requirements
# -t= add a mark image with repository and name
# the trailing . is the path to the Dockerfile. We can also pass a URL
$ docker build -t="bruno/static_web" .
```

It should perform every command in the `Dockerfile` sequencially. At the end, we should have an image listed
```
$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
bruno/static_web        latest              716dfe04f9fb        8 minutes ago       197MB
```

## Caching during docker build
Docker is smart enough to cache each step when bunding the image. 
In the example above, we want to make sure the `apt-get update` command is always executed, so we have to run the build command with `--no-cache` flag.
```sh
$ docker build --no-cache -t="bruno/static_web" .
``` 

## Binding container port to host
We can bind a port in the host machine to the container like this
```sh
$ docker run -d -p 8080:80 --name static_web_8080 bruno/static_web nginx -g "daemon off;"
```
Go to your localhost:8080 and check the result