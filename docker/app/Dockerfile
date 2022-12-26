FROM python:3.9

WORKDIR /usr/app/src

COPY ["./src/", "./"]
COPY ["./data/*.json", "./data/"]

#copy and install requirements.txt
COPY ./requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
#COPY . /tmp/

#copy unit tests and run them
COPY ["./tests/", "./"]
#RUN python -m unittest test_connector.py
