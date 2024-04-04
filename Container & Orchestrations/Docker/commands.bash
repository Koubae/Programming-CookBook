

### ------------------------------
## BUILD
### ------------------------------
docker build -t <IMAGE_NAME> . 
docker build --tag=<IMAGE_NAME> . 

# Targets
docker build --tag=buildme-client --target=client .
docker build --tag=buildme-server --target=server .

# Send build to log
docker build --target=client --progress=plain . 2> log1.txt
# Build Argument https://docs.docker.com/build/guide/build-args/
docker build --build-arg="GO_VERSION=1.19" .
docker build --target=server --build-arg="APP_VERSION=v0.0.1" --tag=buildme-server .
# Export Docker build into a binary https://docs.docker.com/build/guide/export/
docker build --output=. --target=server .
docker build --output=bin --target=binaries .
# Multi-Platform / Emulation https://docs.docker.com/build/guide/multi-platform/
docker build --target=server --platform=linux/arm/v7 .

### ------------------------------
## RUN
### ------------------------------
docker run -ti --name=interactive-container alpine

docker run -p <POST_HOST:PORT_CONTAINER> <IMAGE_NAME>
# Docker welcome 
docker run -d -p 8089:80 --name welcome-to-docker docker/welcome-to-docker
# image build 
docker run -it -p 8000:3000 --name docker-1 welcome-to-docker


# Start container interactive
docker run -it <IMAGE_NAME> sh
docker run -it <IMAGE_NAME> bash
# Detach
docker run -d IMAGE

## Remove container
docker rm <CONTAINER_NAME>

### ------------------------------
## Image
### ------------------------------
# remove all untagged images by combining docker rmi with the recent dangling=true query
# Docker won’t be able to remove images that are behind existing containers, so you may have to remove stopped containers with docker rm first:
docker rm `docker ps --no-trunc -aq`
docker images -q --filter "dangling=true" | xargs docker rmi
# Prune
docker builder prune -af

### 
### History
docker image history getting-started
# Remove line truncation
docker image history --no-trunc getting-started


### ------------------------------
## dociker-compose
### ------------------------------
docker compose down
# remove volumes
docker compose down --volumes


### ------------------------------
## Volume
### ------------------------------
docker volume create todo-db
docker volume inspect todo-db
docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started
# (git bash)
docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=todo-db, target=//etc/todos getting-started

# Using bind mounts
docker run -it --mount type=bind,src="$(pwd)",target=/src ubuntu bash

docker run -dp 127.0.0.1:3000:3000 \
    -w /app --mount type=bind,src="$(pwd)",target=/app \
    node:18-alpine \
    sh -c "yarn install && yarn run dev"


### ------------------------------
## Network
### ------------------------------
docker network create todo-app
docker run -d \
    --network todo-app --network-alias mysql \
    -v todo-mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=todos \
    mysql:8.0


### ------------------------------
## Debug & Toosl
### ------------------------------
# Start a new container using the nicolaka/netshoot image. Make sure to connect it to the same network.
docker run -it --network todo-app nicolaka/netshoot