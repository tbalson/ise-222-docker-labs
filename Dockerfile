FROM ubuntu:latest

MAINTAINER Tyler Balson "tbalson@iu.edu"

RUN apt-get update -y
RUN apt-get install -y apt-utils
RUN apt-get install -y git-core
RUN apt-get install -y curl

RUN apt install -y python3.7
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 10
RUN update-alternatives --config python
RUN apt-get install -y python3.7-distutils
RUN apt-get install -y python3.7-dev
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py 

RUN pip install -U pip

RUN git clone https://github.com/tbalson/ise-222-docker-labs.git
RUN cd ise-222-docker-labs
WORKDIR ise-222-docker-labs
RUN pip install -r requirements.txt 
EXPOSE 8080
#ENTRYPOINT ["python"]
CMD ["bash"]

