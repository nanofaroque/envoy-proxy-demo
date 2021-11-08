docker stop `docker ps -q`
docker image rm -rf ofaroque/green
docker build . -t ofaroque/green
containerId=$(docker run -p 3000:3000 -d ofaroque/green)
docker logs $containerId