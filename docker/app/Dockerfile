FROM python:3.9

# RUN pip install mysql-connector-python
# RUN pip install click

WORKDIR /usr/app/src

COPY ["./", "./"]
#RUN pip install -r requirements.txt

#copy and install requirements.txt
COPY ./requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

#copy and run pre-commit
# COPY ./pre-commit-config.yaml .
# RUN git init . && pre-commit install-hooks
