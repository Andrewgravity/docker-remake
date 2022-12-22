import logging
import json
from connector import Connector
from json2xml import json2xml


class Repository:
    """
    Service used to make queries to the sql database, contains main application methods.
    """

    def __init__(self, output_format: str) -> None:
        self._output_format = output_format

    def fetchAndMapJson(self, cursor: object) -> str:
        """
        Method which makes a json out of column names and row values
        """

        row_headers = [
            x[0] for x in cursor.description
        ]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json_data

    def rooms_and_num_of_students(self) -> str:
        """
        Method which returns a list of rooms and a number of students in them.
        :return: str
        """

        connection = Connector().connect()
        logging.debug("Made a connection to mysql server")
        cursor = connection.cursor()
        logging.debug("Successfully created a cursor")

        cursor.execute(
            """
            SELECT COUNT(1) AS Number_of_students, Student.RoomId
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Student.RoomId;
            """
        )

        json_file = self.fetchAndMapJson(cursor)
        if self._output_format == "xml":
            logging.info("Output format is xml:")
            return json2xml(json_file)

        logging.info("Output format is json:")
        return json_file

    def lowest_avg_age(self) -> str:
        """
        Method which returns 5 rooms with the lowest average age among stundents.
        :return: str
        """

        connection = Connector().connect()
        logging.debug("Made a connection to mysql server")
        cursor = connection.cursor()
        logging.debug("Successfully created a cursor")

        cursor.execute(
            """
            SELECT Room.Id, AVG(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) AS age
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Room.Id
            ORDER BY age ASC
            LIMIT 5;
        """
        )

        json_file = self.fetchAndMapJson(cursor)
        if self._output_format == "xml":
            logging.info("Output format is xml:")
            return json2xml(json_file)

        logging.info("Output format is json:")
        return json_file

    def biggest_age_diff(self) -> str:
        """
        Method which returns 5 rooms with the biggest difference in age among students.
        :return: str
        """

        connection = Connector().connect()
        logging.debug("Made a connection to mysql server")
        cursor = connection.cursor()
        logging.debug("Successfully created a cursor")

        cursor.execute(
            """
            SELECT Room.Id, MAX(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) - MIN(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) AS age
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Room.Id
            ORDER BY age ASC
            LIMIT 5;
        """
        )

        json_file = self.fetchAndMapJson(cursor)
        if self._output_format == "xml":
            logging.info("Output format is xml:")
            return json2xml(json_file)

        logging.info("Output format is json:")
        return json_file

    def rooms_with_diff_genders(self) -> str:
        """
        Method which returns a list of rooms where students with different genders reside.
        :return: str
        """

        connection = Connector().connect()
        logging.debug("Made a connection to mysql server")
        cursor = connection.cursor()
        logging.debug("Successfully created a cursor")

        cursor.execute(
            """
            SELECT COUNT(1) as num_of_students_in_a_room, Room.Id, Room.Name
            FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
            GROUP BY Room.Id, Room.Name
            HAVING COUNT(DISTINCT(Student.Sex)) > 1;
        """
        )

        json_file = self.fetchAndMapJson(cursor)
        if self._output_format == "xml":
            logging.info("Output format is xml:")
            return json2xml(json_file)

        logging.info("Output format is json:")
        return json_file
