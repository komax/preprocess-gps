#!/usr/bin/env python

import os
import sys

args = sys.argv[1:]

def generate_gpx():
    assert len(args) >= 1
    csv_file = args[0]
    assert csv_file.endswith('.csv')

    command_string = 'gpsbabel -i iblue747 -f 003-239.csv -o gpx -F 003-239.gpx'
    os.system(command_string)

def main():
    pass

if __name__ == '__main__':
    main()

