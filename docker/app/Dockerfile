FROM python:3.9

RUN pip install mysql-connector-python
RUN python -m pip install lxml

WORKDIR /usr/app/src

#COPY ./../data/*.json ./
COPY ["./data/students.json", "./data/rooms.json", "./"]

#ADD ./../../src/ src
COPY ["./main.py", "insert_values.py", "connect_to_sql.py", "sql_queries.py", "xml_converter.py", "./"]

#ENTRYPOINT [ "python3", "insert_values.py", "main.py" ]