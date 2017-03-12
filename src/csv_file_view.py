# written by Pippa Crawshaw
# input and output related to using a csv file

from view import View
import csv


class CsvFileView(View):
    def __init__(self):
        pass

    def output(self, file_reader):
        for row in file_reader:
            print(', '.join(row))

    def get_input(self, file_name):
        read_csv = ""
        with open(file_name, newline='') as file:
            # the csv file is converted to lists of lists
            # csv.reader does not retain information once the file is closed
            read_csv = list(csv.reader(file, delimiter=','))
        return read_csv

    def start(self):
        print('Assignment One PR301 Semester One 2017')

    def stop(self):
        print('Goodbye!')
