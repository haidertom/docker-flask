# Python Flask app inside Docker container

This is a minimal example of how you can dockerize your python app and how files can be transferred using flask and a rest api.
Simply put everything you need inside the container and this is how you can properly acess it from the outside.

### usage

You will need Docker running on your system. Then we can use the `docker-compose` command to build the image and spin up the container:

`docker-compose up` 

This will build the image as specified in the Dockerfile (pull the ubuntu base image, install python, copy the folder to the container and intall the specified requirements) and start the containers along with some specifications. The entrypoint just specifies what happens by default when we start a container from this image. We will also bind-mound the local folder to the folder in the container. Any changes you make in the app will therefore be directly visible. For details on what happens exactly just inspect the `docker-compose.yml` file.

For the client, we also need some python requirements.

`python3 -m pip install requests jsonpickle pillow numpy matplotlib`

Finally you can run your client application:

`python3 client.py`

This is just a simple example, the client can be written in any language of course. Here we just transfer an image back and forth along with some additional data created inside the container. 



