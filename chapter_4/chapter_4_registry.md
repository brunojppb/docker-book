# Docker Registry

If we want to create our own images with private information we either:

- Use the Docker hub with private (paid) repositories
- Run our own registry

Using the open-source registry provided by Docker inc., we can run our own registry in-house.

Lets create container based on the Docker registry image:
```sh
$ docker run -d -p 5000:5000 --name registry registry:2
```

Now that we have our Docker registry running, I will tag my image `bruno/static_web` based on its ID and a hostname (just set for testing)
```sh
$ docker tag 9081eb928c1a docker.example.com:5000/bruno/static_web
```

Now we can push this image to our own registry:
```sh
$ docker push docker.example.com:5000/bruno/static_web
```

Notice that there is no authentication in place. It must be set during the registry setup. Take a look in the [Registry Deployment Setup](https://docs.docker.com/registry/deploying/)