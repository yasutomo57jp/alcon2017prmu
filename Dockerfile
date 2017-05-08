FROM continuumio/miniconda3:latest

MAINTAINER kawanishi

RUN apt update
RUN apt install -y libopencv-dev
RUN conda create -n alcon python=3.6 anaconda-client
RUN ["/bin/bash", "-c", "source activate alcon && conda install -y numpy scipy ipython scikit-learn matplotlib opencv tensorflow keras"]
RUN echo "source activate alcon" > /root/.bashrc

