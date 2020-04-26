docker container run \
    -it \ # interactive mode
    --rm \ # remove container after done
    -p 5007:5007 \ # expose and forward the port for http
    -v $(pwd)/flaskapp:/flaskapp \ # bind local folder to container so changes will get updated continously
    -w /flaskapp \ # specify the working directory inside the container
    --name flaskapp_container \ # specify the name of the container in which the server will run
    flaskapp:latest # specify the image we want to use