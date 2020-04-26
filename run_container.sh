docker container run \
    -it \
    --rm \
    -p 5007:5007 \
    -v $(pwd)/flaskapp:/flaskapp \
    -w /flaskapp \
    --name flaskapp_container \
    flaskapp:latest

 # -it interactive mode
 # --rm remove container after done
 # -p expose and forward the port for http
 # -v bind local folder to container so changes will get updated continously
 # -w specify the working directory inside the container
 # --name specify the name of the container in which the server will run
 # specify the image we want to use