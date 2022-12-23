import sys

sys.path.append("./../src/")
from json2xml import json2xml
import pytest
import mysql.connector
from unittest.mock import Mock


def test_json2xml():
    data = [{"Id": 661, "age": 15.0}, {"Id": 913, "age": 21.0}]
    result = "<Id>\n\t661\n</Id>\n<age>\n\t15.0\n</age>\n<Id>\n\t913\n</Id>\n<age>\n\t21.0\n</age>"
    assert json2xml(data) == result
