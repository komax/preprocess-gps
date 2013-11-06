#!/usr/bin/env python3

import os
import sys
import glob

def merge_gpx(directory_name, out_file):
    parameter_str = ''
    for gpx_file in glob.glob(directory_name+'/*.gpx'):
        parameter_str += ' -f %s' % (gpx_file)

    if not parameter_str:
        return

    command_string = "gpsbabel -i gpx %s -o gpx -F %s" %\
      (parameter_str, out_file)
    print(command_string)
    os.system(command_string)

def main():
    args = sys.argv[1:]
    assert len(args) >= 1
    (dir_name, out_file) = args[0:2]
    if os.path.isdir(dir_name):
        merge_gpx(dir_name, out_file)

if __name__ == '__main__':
    main()

