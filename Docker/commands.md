# Docker introduction
- Docker Images: It is a bunch of programs with dependancies and libraiers. Ex: Ubuntu image, ROS image
- Docker container: It is used to run an docker image.
## Docker commands
### Docker image
Look into various images
```
docker image ls
```

Pull images from online (ros humble version)
```
docker image pull ros:humble
```

delete a image from the system
```
docker image rm -f name
```
Run a docker image
```
docker run -it ros:humble
```
### Docker containers
Look into various containers in the system
```
docker container ls 

docker ps

# it also shows the ones closed
docker ps -a
```

Start the container name
```
docker container start -i name
```

Stop the container name
```
docker container stop name
```
Delete the container
```
docker container rm name

# Delete all the containers
docker container prune
```
Open the terminal inside a folder
```
docker exec -it name /bin/bash

docker exec -it name ls

```
## Writing a Docker file
- It is efficient to write a docker file for running.
- It is done by creating [Dockerfile](https://www.youtube.com/watch?v=SAMPOK_lazw&t=179s&ab_channel=ArticulatedRobotics).
- Here is an example where ROS humble is ran and some commands are run.
- It also will copy config files from the local folder to the image.

```
FROM ros:humble

RUN apt-get update && apt-get install -y nano && rm -rf /var/lib/apt/lists/*

COPY config/ /site_config/

```
Once the file is ready, we first build it.
```
docker build -t my_image .
```
After the file is ready, we run it.
```
docker run -it my_image
```