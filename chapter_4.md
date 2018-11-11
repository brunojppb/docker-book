## Docker Images

A image is a `ready only` stack with whatever dependecy we need that can be used as base for our containers.

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

