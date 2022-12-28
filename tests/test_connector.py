import sys

sys.path.append("./../src/")
from connector import Connector
import pytest
import mysql.connector
from unittest.mock import Mock


@pytest.fixture
def test_connector():
    mock = Mock(Connector())
    return mock


@pytest.fixture
def test_connect(test_connector):
    try:
        test_connector.connect()
    except mysql.connector.Error as err:
        print(f"couldn't connect to server: {err}")


def test_cursor(test_connector):
    try:
        test_connector.connect().cursor()
    except mysql.connector.Error as err:
        print(f"couldn't create cursor: {err}")
