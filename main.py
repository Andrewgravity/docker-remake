import logging
logging.basicConfig(level=logging.DEBUG)
logging.info('Starting main.py')

from python import Queries
# import mysql.connector
# import json



Queries().query_1()
Queries().query_2()
Queries().query_3()
Queries().query_4()
print(Queries().query_1())
print(Queries().query_2())
print(Queries().query_3())
print(Queries().query_4())