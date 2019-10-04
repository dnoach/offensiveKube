FROM debian
MAINTAINER Aviad Noah

# upgrade distro 
RUN apt-get update && apt-get install apt-file -y && apt-file update && apt-get install vim -y && apt-get install nmap
RUN apt-get install python
RUN apt-get clean
COPY test.py /
