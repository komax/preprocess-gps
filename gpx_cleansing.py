#!/usr/bin/env python3

import os
import glob
import argparse


def clean_up_gpx(gpx_file_name, epsilon, out_dir):
    assert gpx_file_name.endswith('.gpx')
    (in_dir, file_name) = os.path.split(gpx_file_name)

    out_file_name = out_dir + '/' + file_name[:-4] + '_dropped_outliers.gpx'
    filter_option = "discard,hdop=%s,vdop=%s,hdopandvdop" % epsilon
    command_string = \
        "gpsbabel -i gpx -f %s -x %s -o gpx -F %s" %\
        (gpx_file_name, filter_option, out_file_name)
    print(command_string)
    os.system(command_string)
    return


def apply_on_gpx_directory(directory, function, *fun_args):
    for gpx_file in glob.glob(directory + '/*.gpx'):
        function(gpx_file, *fun_args)
    return


def clean_up_gpx_directory(directory, epsilon, out_dir):
    return apply_on_gpx_directory(directory, clean_up_gpx, epsilon, out_dir)


def is_gpxpy_installed():
    try:
        import gpxpy
        return True
    except ImportError:
        return False


def simplify_gpx(gpx_file_name, alpha_error, out_dir, select_gpsbabel=False):
    assert gpx_file_name.endswith('.gpx')
    (in_dir, file_name) = os.path.split(gpx_file_name)
    out_file_name = "%s/%s_simplified_d_%i.gpx" %\
                    (out_dir, file_name[:-4], alpha_error)

    if select_gpsbabel:
        selection_method = False
    else:
        selection_method = is_gpxpy_installed()

    if selection_method:
        # Use gpxpy package.
        import gpxpy
        with open(gpx_file_name, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
            gpx.simplify(alpha_error)
            with open(out_file_name, 'w') as out_file:
                print("writing file: %s" % out_file_name)
                out_file.write(gpx.to_xml())
    else:
        # Use gpsbabel on the commandline.
        alpha_in_kilometers = alpha_error / 1000
        filter_option = "simplify,error=%sk" % alpha_in_kilometers
        command_string = "gpsbabel -i gpx -f %s -x %s -o gpx -F %s" %\
                         (gpx_file_name, filter_option, out_file_name)
        print(command_string)
        os.system(command_string)
    return


def simplify_gpx_directory(directory, alpha_error, out_dir):
    return apply_on_gpx_directory(directory, simplify_gpx,
                                  alpha_error, out_dir)


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
    parser.add_argument('-s', '--simplify', type=int,
                        help='Apply Douglas-Peuker filter')
    parser.add_argument('-o', '--out-dir', type=str, default='.',
                        help='directory to write the data in')
    args = parser.parse_args()
    dir_name = args.input
    if args.drop_outlier:
        if os.path.isdir(dir_name):
            clean_up_gpx_directory(dir_name, args.drop_outlier, args.out_dir)
        else:
            clean_up_gpx(dir_name, args.drop_outlier, args.out_dir)
    if args.simplify:
        if os.path.isdir(dir_name):
            simplify_gpx_directory(dir_name, args.simplify, args.out_dir)
        else:
            simplify_gpx(dir_name, args.simplify, args.out_dir)
