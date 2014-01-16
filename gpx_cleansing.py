#!/usr/bin/env python3

import sys
import os
import glob


def clean_up_gpx(gpx_file_name):
    assert gpx_file_name.endswith('.gpx')
    # TODO real implementation
    pass


def clean_up_gpx_directory(dir_name):
    for gpx_file in glob.glob(dir_name+'/*.gpx'):
        clean_up_gpx(gpx_file)
    return


if __name__ == '__main__':
    args = sys.argv[1:]
    assert len(args) >= 1
    dir_name = args[0]
    if os.path.isdir(dir_name):
        clean_up_gpx_directory(dir_name)
    else:
        clean_up_gpx(dir_name)