FROM ubuntu:20.04

# install python
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-dev -y 
RUN apt-get install python3-pip -y

# copy the folder into the container and install requirements
COPY flaskapp /flaskapp
RUN pip3 --no-cache-dir install -r /flaskapp/requirements.txt

#ENTRYPOINT
CMD ["python3", "run.py"]
