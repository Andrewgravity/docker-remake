import logging
import json
from connect_to_sql import Connector

# logging.basicConfig(level=logging.DEBUG)
# logging.info('Starting queries.py')

class Queries:

    def __init__(self) -> None:
        pass

    def query_1(self) -> object:
        # establish connection to SQL server
        # connection = Connection()
        # cursor = connection.cursor()
        # connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
        # print('Database connected, executing query 1')
        # cursor = connection.cursor()
        connection = Connector().connect()
        logging.debug('Made a connection to mysql server')
        cursor = connection.cursor()
        logging.debug('Successfully created a cursor')

        cursor.execute('''
            SELECT COUNT(1) AS Number_of_students, Student.RoomId
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Student.RoomId;
            ''')

        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json_data

    def query_2(self) -> object:
        # establish connection to SQL server
        # connection = Connection()
        # cursor = connection.cursor()
        # connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
        # print('Database connected, executing query 2')
        # cursor = connection.cursor()
        connection = Connector().connect()
        logging.debug('Made a connection to mysql server')
        cursor = connection.cursor()
        logging.debug('Successfully created a cursor')

        cursor.execute('''
            SELECT Room.Id, AVG(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) AS age
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Room.Id
            ORDER BY age ASC
            LIMIT 5;
        ''') 

        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json_data

    def query_3(self) -> object:
        # establish connection to SQL server
        # connection = Connection()
        # cursor = connection.cursor()
        # connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
        # print('Database connected, executing query 3')
        # cursor = connectio
        connection = Connector().connect()
        logging.debug('Made a connection to mysql server')
        cursor = connection.cursor()
        logging.debug('Successfully created a cursor')

        cursor.execute('''
            SELECT Room.Id, MAX(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) - MIN(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) AS age
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Room.Id
            ORDER BY age ASC
            LIMIT 5;
        ''')    

        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json_data

    def query_4(self) -> object:
        # establish connection to SQL server
        # connection = Connection()
        # cursor = connection.cursor()
        # connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
        # print('Database connected, executing query 4')
        # cursor = connection.cursor()
        connection = Connector().connect()
        logging.debug('Made a connection to mysql server')
        cursor = connection.cursor()
        logging.debug('Successfully created a cursor')

        cursor.execute('''
            SELECT COUNT(1) as num_of_students_in_a_room, Room.Id, Room.Name
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Room.Id, Room.Name
            HAVING COUNT(DISTINCT(Student.Sex)) > 1
        ''')    

        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json_data