

# remove all untagged images by combining docker rmi with the recent dangling=true query
# Docker won’t be able to remove images that are behind existing containers, so you may have to remove stopped containers with docker rm first:
docker rm `docker ps --no-trunc -aq`
docker images -q --filter "dangling=true" | xargs docker rmi