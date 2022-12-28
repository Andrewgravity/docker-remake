import mysql.connector
import os
import logging
from dotenv import load_dotenv
from json2xml import json2xml

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
        load_dotenv()
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        connection = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name,
        )
        return connection

    def cursor(self) -> object:
        """
        Method that creates a cursor to fetch data from mysql database.
        """
        connection = self.connection()
        cursor = connection.cursor()
        return cursor
