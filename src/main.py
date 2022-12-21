import logging
import click

#from lxml import etree
from uploader import Uploader
from repository import Repository
from json2xml import json2xml

logging.basicConfig(level=logging.DEBUG)
logging.info('Starting main.py')

@click.command
@click.option(
    "-r",
    "--rooms-path",
    default = './data/rooms.json',
    help="Path to file with data about rooms",
    type=click.STRING
)
@click.option(
    "-s",
    "--students-path",
    default = './data/students.json',
    help="Path to file with data about students",
    type=click.STRING,
)
@click.option(
    "-f",
    "--output-format",
    default = "xml",
    help="Output file format",
    type=click.Choice(["json", "xml"]),
)

def main(rooms_path: str, students_path: str, output_format: str) -> None:

    Uploader(rooms_path, students_path).start()

    Repository(output_format).rooms_and_num_of_students()
    Repository(output_format).lowest_avg_age()
    Repository(output_format).biggest_age_diff()
    Repository(output_format).rooms_with_diff_genders()
    print(Repository(output_format).rooms_and_num_of_students())
    print(Repository(output_format).lowest_avg_age())
    print(Repository(output_format).biggest_age_diff())
    print(Repository(output_format).rooms_with_diff_genders())

    logging.info('main.py executed')

if __name__ == "__main__":
    main()