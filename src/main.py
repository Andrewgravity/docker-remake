import logging
logging.basicConfig(level=logging.DEBUG)
logging.info('Starting main.py')

from lxml import etree
from insert_values import Uploader
from sql_queries import Queries
from xml_converter import json2xml
# import mysql.connector
# import json


def main(rooms_path: str, students_path: str, output_path: str, output_format: str) -> None:

    Uploader().start()

    Queries().query_1()
    Queries().query_2()
    Queries().query_3()
    Queries().query_4()
    print(Queries().query_1())
    print(Queries().query_2())
    print(Queries().query_3())
    print(Queries().query_4())

    print(json2xml(Queries().query_3()))
    print(type(Queries().query_3()))

if __name__ == "__main__":
    main("a","b","c","D")