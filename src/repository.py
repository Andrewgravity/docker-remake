import logging
import json
from connector import Connector
from combiner import Combiner
from json2xml import json2xml

class Repository:

    def __init__(self, output_format) -> None:
        self._output_format = output_format

    def rooms_and_num_of_students(self) -> object:

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

        # return XML
        if self._output_format == 'xml':
            logging.info('Output format is xml:')
            return json2xml(json_data)

        logging.info('Output format is json:')
        return json_data

    def lowest_avg_age(self) -> object:

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

        # return XML
        if self._output_format == 'xml':
            logging.info('Output format is xml:')
            return json2xml(json_data)

        logging.info('Output format is json:')
        return json_data

    def biggest_age_diff(self) -> object:

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

        # return XML
        if self._output_format == 'xml':
            logging.info('Output format is xml:')
            return json2xml(json_data)
        
        logging.info('Output format is json:')
        return json_data

    def rooms_with_diff_genders(self) -> object:

        connection = Connector().connect()
        logging.debug('Made a connection to mysql server')
        cursor = connection.cursor()
        logging.debug('Successfully created a cursor')

        cursor.execute('''
            SELECT COUNT(1) as num_of_students_in_a_room, Room.Id, Room.Name
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Room.Id, Room.Name
            HAVING COUNT(DISTINCT(Student.Sex)) > 1;
        ''')    

        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))

        # return XML
        if self._output_format == 'xml':
            logging.info('Output format is xml:')
            return json2xml(json_data)

        logging.info('Output format is json:')
        return json_data