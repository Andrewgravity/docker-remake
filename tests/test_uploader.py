import sys

sys.path.append("./../src/")
from uploader import *
import pytest
import mysql.connector
from unittest.mock import Mock


@pytest.fixture
def test_Uploader():
    mock = Mock(Uploader("", ""))
    return mock


def test_start(test_Uploader):
    try:
        test_Uploader.start()
    except mysql.connector.Error as err:
        print("couldn't upload data to the db")
