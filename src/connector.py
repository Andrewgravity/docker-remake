import mysql.connector

# establish connection to SQL server
class Connector:
    """
    Class that performs connections to mysql database.
    """

    def __init__(self) -> None:
        pass

    def connect(self) -> object:
        """
        Method that creates a connection to mysql database.
        """
        connection = mysql.connector.connect(
            user="root", password="root", host="db-server", port="3306", database="db"
        )
        return connection

    def cursor(self) -> object:
        """
        Method that creates a cursor to fetch data from mysql database.
        """
        connection = self.connection()
        cursor = connection.cursor()
        return cursor
