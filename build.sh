docker stop sample || true
docker rm sample || true
docker rmi sample || true
docker build -t sample .
docker run --name sample -p 8100:8101 -d --restart always --network dockers_default -e MONGO_URL=mongodb://mongodb:27017 -e DB_NAME=sample sample
