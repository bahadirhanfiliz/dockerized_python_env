# dockerized_python_env
This is a demo project to show how to create Dockerized Python Environments.

## Docker Commands
#### Build docker image
```
docker build python_env .
```

#### Run docker container
```
# During development
docker run -v /<aboslute path>/dockerized_python_env:/app python_env

# During prod
docker run python_env
```

During development in order not the build the image over and over again.
-v comamnd bind mounts the project directory to containers project directory. 
Hence, you can re-start the container in to run your newly saved code.