from connector import Connector
import json
import logging


class Uploader:
    """
    Class used to upload data to sql database, contains main application methods.
    """

    def __init__(self, rooms_path, students_path) -> None:
        self._rooms_path = rooms_path
        self._students_path = students_path

    def start(self) -> None:
        """
        Method for file opening nad values insertion.
        :return: None
        """

        logging.basicConfig(level=logging.DEBUG)
        logging.info("Starting uploader.py")

        # read students data from json
        with open(self._students_path, "r") as read_file:  #'./data/students.json'
            students_data = json.load(read_file)
        logging.info("Students data read")

        # read rooms data from json
        with open(self._rooms_path, "r") as read_file:  #'./data/rooms.json'
            rooms_data = json.load(read_file)
        logging.info("Rooms data read")

        # connect to mysql server
        connection = Connector().connect()
        logging.debug("Made a connection to mysql server")
        cursor = connection.cursor()
        logging.debug("Successfully created a cursor")

        # insert values into rooms table
        for item in rooms_data:
            id = item.get("id")
            name = item.get("name")
            cursor.execute("INSERT INTO Room(Id, Name) VALUES(%s, %s)", (id, name))
        logging.info("Rooms data was input into Rooms table")

        # insert values into students tables
        for item in students_data:
            birthday = item.get("birthday")
            id = item.get("id")
            name = item.get("name")
            room = item.get("room")
            sex = item.get("sex")
            cursor.execute(
                "INSERT INTO Student(Birthday, Id, Name, RoomId, Sex) VALUES(%s,%s,%s,%s,%s)",
                (birthday, id, name, room, sex),
            )
        logging.info("Students data was input into Students table")

        # commit the input data
        connection.commit()
        logging.debug("All input data was commited to server")
