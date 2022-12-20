FROM python:3.9

RUN pip install mysql-connector-python
# RUN apt-get update \
#     && apt-get -y install libpq-dev gcc \
#     && pip install psycopg2

WORKDIR /usr/app/src

COPY ["/data/students.json", "/data/rooms.json", "./"]
#COPY *.json ./
#COPY insert_values.py ./
COPY ["/python/connect_to_sql.py", "/python/insert_values.py", "/python/sql_queries.py", "main.py", "./"]

#ENTRYPOINT [ "python3", "insert_values.py", "main.py" ]