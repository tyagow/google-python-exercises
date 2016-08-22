#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import glob
import re
import os
import shutil
import subprocess
import zipfile

"""Copy Special exercise

"""


def get_special_paths(dir):
    return glob.glob(dir + "/*__*.*")


def copy_to(dirs, dir_to_send):
    for dir in dirs:
        shutil.move(dir, dir_to_send)


def zip_files(dirs, dir_to_send):
    # path = ''
    # for dir in dirs:
    #     path += dir + " "
    #
    # print("-j tmp.zip " + path)
    # try:
    #     subprocess.call(["zip", "-j tmp.zip '" + path + "'"])
    #     # zip -j tmp.zip path
    # except IOError:
    #     print('error')
    with zipfile.ZipFile('tmp.zip', mode='w') as zf:
        zf.debug = 3
        for dir in dirs:
            zf.write(dir)

    for name in zf.namelist():
        print(name)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

        # +++your code here+++
        # Call your functions
    dir_origin = args[1]
    dirs = get_special_paths(dir_origin)
    if not todir == '':
        copy_to(dirs, todir)
    # elif not tozip == '':
        # zip_files(dirs, todir)


if __name__ == "__main__":
    main()
