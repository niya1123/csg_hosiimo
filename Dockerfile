FROM python:3.7

RUN mkdir /csg_hosiimo

WORKDIR /csg_hosiimo 

ADD ./ /csg_hosiimo

RUN pip install pipenv &&\
    pipenv install &&\
    pipenv install --dev