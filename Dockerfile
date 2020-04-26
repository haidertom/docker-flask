FROM ubuntu:20.04

# install python
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-dev -y 
RUN apt-get install python3-pip -y

#copy the requirements file and install the rest of the requirements, clean up after done
COPY flaskapp/requirements.txt /tmp/requirements.txt
RUN pip3 --no-cache-dir install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

#ENTRYPOINT
CMD ["python3", "run.py"]
