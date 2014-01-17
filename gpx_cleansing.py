#!/usr/bin/env python3

import os
import glob
import argparse


def clean_up_gpx(gpx_file_name, precision):
    (file_name, file_ext) = os.path.splitext(gpx_file_name)
    assert file_ext == '.gpx'

    out_file_name = file_name + '_dropped_outliers' + file_ext
    filter_option = "discard,hdop=%s,vdop=%s,hdopandvdop" % precision
    command_string = \
        "gpsbabel -i gpx -f %s -x %s -o gpx -F %s" %\
        (gpx_file_name, filter_option, out_file_name)
    print(command_string)
    os.system(command_string)
    return


def clean_up_gpx_directory(directory, precision):
    for gpx_file in glob.glob(directory + '/*.gpx'):
        clean_up_gpx(gpx_file, precision)
    return


def precision(s):
    try:
        hdop, vdop = map(int, s.split(','))
        return hdop, vdop
    except:
        raise argparse.ArgumentTypeError('hdop,vdop must be integers')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
        Collection of GPS Processing to clean/simplify the data:
        1. Detect outlier and drop them.
        2. Apply Douglas-Peuker filter to simplify the GPS data
    ''')
    parser.add_argument('input', type=str,
                        help='input gpx file or directory')
    parser.add_argument('-d', '--drop-outlier', type=precision,
                        help='detect and drop outliers hdop,vdop')
    args = parser.parse_args()
    dir_name = args.input
    print(args.drop_outlier)
    if args.drop_outlier:
        if os.path.isdir(dir_name):
            clean_up_gpx_directory(dir_name, args.drop_outlier)
        else:
            clean_up_gpx(dir_name, args.drop_outlier)