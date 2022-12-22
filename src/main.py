import logging
import click
from uploader import Uploader
from repository import Repository
from json2xml import json2xml

logging.basicConfig(level=logging.DEBUG)
logging.info("Starting main.py")


@click.command
@click.option(
    "-r",
    "--rooms-path",
    default="./src/data/rooms.json",
    help="Path to file with data about rooms",
    type=click.STRING,
)
@click.option(
    "-s",
    "--students-path",
    default="./src/data/students.json",
    help="Path to file with data about students",
    type=click.STRING,
)
@click.option(
    "-f",
    "--output-format",
    default="json",
    help="Output file format",
    type=click.Choice(["json", "xml"]),
)
def main(rooms_path: str, students_path: str, output_format: str) -> None:

    """
    Main application, uploads data to the database by running an Uploader object method and then makes all the necessary
    sql queries running the Repository object methods.
    :param rooms_path: pathfile to rooms data
    :param students_path: pathfile to students data
    :param output_format: the output format: json or xml
    :return: None
    """

    Uploader(rooms_path, students_path).start()

    rooms_and_num_of_students = Repository(output_format).rooms_and_num_of_students()
    lowest_avg_age = Repository(output_format).lowest_avg_age()
    biggest_age_diff = Repository(output_format).biggest_age_diff()
    rooms_with_diff_genders = Repository(output_format).rooms_with_diff_genders()
    print(rooms_and_num_of_students)
    print(lowest_avg_age)
    print(biggest_age_diff)
    print(rooms_with_diff_genders)

    logging.info("main.py executed")


if __name__ == "__main__":
    main()
