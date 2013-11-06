#!/usr/bin/env python

import os
import sys

args = sys.argv[1:]

def generate_gpx():
    assert len(args) >= 1
    csv_file = args[0]
    (file_name, file_ext) = os.path.splitext(csv_file)
    assert file_ext == '.csv'
    assert csv_file.endswith('.csv')

    command_string = "gpsbabel -i iblue747 -f %s.csv -o gpx -F %s.gpx" %\
      (file_name, file_name)
    print command_string
    os.system(command_string)

def main():
    generate_gpx()

if __name__ == '__main__':
    main()

