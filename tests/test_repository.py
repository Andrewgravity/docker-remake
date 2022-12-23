import sys

sys.path.append("./../src/")
from repository import *
import pytest
import mysql.connector
from unittest.mock import Mock


@pytest.fixture
def test_cursor():
    mock = Mock(Connector())
    connect = mock.connect()
    cursor = connect.cursor()
    return cursor


@pytest.fixture
def test_repository():
    mock = Mock(Repository(""))
    return mock


def test_fetchAndMapJson(test_cursor, test_repository):
    try:
        test_repository.fetchAndMapJson(test_cursor)
    except mysql.connector.Error as err:
        print("couldn't connect to server: {}".format(err))


def test_rooms_and_num_of_students(test_repository):
    try:
        test_repository.rooms_and_num_of_students()
    except:
        print("couldnt fetch a query")


def test_lowest_avg_age(test_repository):
    try:
        test_repository.test_lowest_avg_age()
    except:
        print("couldnt fetch a query")


def biggest_age_diff(test_repository):
    try:
        test_repository.biggest_age_diff()
    except:
        print("couldnt fetch a query")


def rooms_with_diff_genders(test_repository):
    try:
        test_repository.rooms_with_diff_genders()
    except:
        print("couldnt fetch a query")
