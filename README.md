# Python Flask app inside Docker container

This is a minimal example of how you can dockerize your python app and how files can be transferred using flask and a rest api.
Simply put everything you need inside the container and this is how you can properly acess it from the outside.

### usage

You will need Docker running on your system and some basic python packages for the client:

`python3 -m pip install requests jsonpickle pillow numpy matplotlib`

Build the docker image: 

`docker image build -t flaskapp:latest .`

Run the container:

`sh run_container.sh`

This will bind-mound the local folder to the folder in the container. Any changes you make in the app will therefore be directly visible. 
For details on what happens exactly just inspect the shell script.

Finally you can run your client application:

`python3 client.py`




