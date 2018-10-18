docker stop $(docker ps -aq)
docker rm easy2make_web_1
docker rmi easy2make
docker-compose up