FROM ubuntu:latest

MAINTAINER Kate Hodesdon "kate@hodesdon.com"

RUN apt-get update -y && \
    apt-get install -y \ 
    python-pip python-dev build-essential \
    wget git-core
RUN apt-get install -y wget build-essential zlib1g-dev libncurses5-dev
RUN cd /tmp && wget http://www.dabeaz.com/ply/ply-3.9.tar.gz && \
    tar zxfv ply-3.9.tar.gz && cd ply-3.9 && python setup.py install
RUN git clone git://github.com/sympy/sympy.git /sympy &&\
    cd sympy && \
    python setup.py install
RUN git clone https://github.com/satsumas/prop.git /usr/src/prop
WORKDIR /usr/src/prop
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ENTRYPOINT ["python"]
CMD ["prop_yacc.py"]
