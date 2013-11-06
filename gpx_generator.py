#!/usr/bin/env python3

import os
import sys
import glob

def generate_gpx(csv_file):
    (file_name, file_ext) = os.path.splitext(csv_file)
    assert file_ext == '.csv'
    assert csv_file.endswith('.csv')

    command_string = "gpsbabel -i iblue747 -f %s.csv -o gpx -F %s.gpx" %\
      (file_name, file_name)
    print(command_string)
    os.system(command_string)

def main():
    args = sys.argv[1:]
    assert len(args) >= 1
    arg = args[0]
    if os.path.isfile(arg):
        generate_gpx(arg)
    elif os.path.isdir(arg):
        for csv_file in glob.glob(arg+'/*.csv'):
            generate_gpx(csv_file)
    

if __name__ == '__main__':
    main()

