#!/usr/bin/env python3

import os
import sys
import glob
import csv

tmp_file = '/tmp/tmp.csv'


def strip_iblue747(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open(tmp_file, 'w') as stripped_csv:
            csv_writer = csv.writer(stripped_csv, delimiter=',')
            for row in csv_reader:
                #stripped_row = row[0:14] + row[-1:]
                stripped_row = row[0:2] + row[4:6] + row[7:14] + row[-1:]
                csv_writer.writerow(stripped_row)


def generate_gpx(csv_file):
    (file_name, file_ext) = os.path.splitext(csv_file)
    assert file_ext == '.csv'
    assert csv_file.endswith('.csv')
    strip_iblue747(csv_file)

    command_string = "gpsbabel -i iblue747 -f %s -o gpx -F %s.gpx" %\
      (tmp_file, file_name)
    print(command_string)
    os.system(command_string)


if __name__ == '__main__':
    args = sys.argv[1:]
    assert len(args) >= 1
    arg = args[0]
    if os.path.isfile(arg):
        generate_gpx(arg)
    elif os.path.isdir(arg):
        for csv_file in glob.glob(arg+'/*.csv'):
            generate_gpx(csv_file)

