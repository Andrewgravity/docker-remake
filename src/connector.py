import mysql.connector
# establish connection to SQL server
class Connector:

    def __init__(self)  -> None:
        pass

    def connect(self) -> object:
        connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
        return connection

    def cursor(self) -> object:
        connection = self.connection()
        cursor = connection.cursor()
        return cursor
        
    # def description(self) -> object:
    #     cursor = self.cursor()
    #     description = cursor.description()
    #     return description