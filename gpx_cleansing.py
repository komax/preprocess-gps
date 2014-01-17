#!/usr/bin/env python3

import sys
import os
import glob
import argparse


def clean_up_gpx(gpx_file_name):
    assert gpx_file_name.endswith('.gpx')
    # TODO real implementation
    pass


def clean_up_gpx_directory(directory):
    for gpx_file in glob.glob(directory + '/*.gpx'):
        clean_up_gpx(gpx_file)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
        Collection of GPS Processing to clean/simplify the data:
        1. Detect outlier and drop them.
        2. Apply Douglas-Peuker filter to simplify the GPS data
    ''')
    parser.add_argument('input', type=str,
                        help='input gpx file or directory')
    parser.add_argument('-d', '--drop-outlier', action='store_true',
                        default=False)
    args = parser.parse_args()
    dir_name = args.input
    print(args.drop_outlier)
    if os.path.isdir(dir_name):
        clean_up_gpx_directory(dir_name)
    else:
        clean_up_gpx(dir_name)