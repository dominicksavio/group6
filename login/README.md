# login
accounts ,registration,login,logout
# docker
//windows alen
docker container run -d --name=pg -p 5432:5432 -e POSTGRES_PASSWORD=secret -e PGDATA=/pgdata -v /d/Login/login/pgdata:/var/lib/postgresql/data postgres
//linux
sudo docker container run -d --name=pg -p 5432:5432 -e POSTGRES_PASSWORD=secret -e PGDATA=/pgdata -v /home/dominic/Desktop/s8/group\ 6/login/pgdata:/var/lib/postgresql/data postgres

#PGADMIN​
sudo docker run -d -e PGADMIN_DEFAULT_EMAIL="DOMINIC" -e PGADMIN_DEFAULT_PASSWORD="PASSWORD" -p 5555:80 --name pgadmin dpage/pgadmin4

IP
sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id>


sudo docker run -p 5432:5432 -d \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=roadmakerDB \
    -v <pwd>/pgdata:/var/lib/postgresql/data \
    postgres

psql stripe-example -h localhost -U postgres

docker exec -it bdca2b8c09b7 psql -U postgres stripe-example

LINUX
sudo docker run -p 5432:5432 --name=roadMakerContainer -d -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=roadmakerDB -e PGDATA=postgres -v /home/dominic/Desktop/s8/group\ 6/login/pgdata:/postgres -i ps_image_with_data

sudo docker tag dominicksavio/roadmaker:v1 dominicksavio/roadmakerpostgres:v1
sudo docker push dominicksavio/roadmakerpostgres:v1

sudo docker run -d \
    --name roadMakerContainer \
    -p 5432:5432 \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=roadmakerDB \
    -e POSTGRES_PASSWORD=postgres \
    -e PGDATA=postData \
    dominicksavio/roadmakerpostgres:latest

    -v /home/dominic/Desktop/s8/group\ 6/pgdata:/postData \