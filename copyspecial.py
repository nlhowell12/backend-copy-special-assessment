#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse
import glob
"""Copy Special exercise
"""

# Write functions and modify main() to call them
def find_special_paths(dir):
    """Finds an files that contain the a string matching "__Word__" """
    found = filter(re.compile(r'__\w+__').search, glob.glob('*.*'))
    for i, filename in enumerate(found):
        found[i] = os.path.abspath(filename)
    return found

def copy_to(paths, dir):
    """Copies files from the given paths to the provided directory"""
    count = 0
    if not os.path.exists(dir):
        os.mkdir(dir)
    for filepath in paths:
        count += 1
        shutil.copy(filepath, dir)
    print "Copied {} files to {}".format(count, dir)

def zip_to(paths, zippath):
    """Creates a zip file of the files found at the path provided"""
    files = ""
    for filepath in paths:
        files += filepath + " "
    print "Command I'm going to do:"
    new_zip =  "zip -j" + " " + zippath + " " + files
    print new_zip
    result, output = commands.getstatusoutput(new_zip)
    if result:
        print output
        sys.exit(1)
    return


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='specifies directory to grab special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    if not args:
        parser.print_usage()
        sys.exit(1)
    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).
    
    # +++your code here+++
    # Call your functions
    if args.from_dir:
        os.chdir(args.from_dir)
    if not args.todir and not args.tozip:
        for filename in find_special_paths(os.getcwd()):
            print filename
    if args.todir:
        copy_to(find_special_paths(os.getcwd()), args.todir)
    if args.tozip:
        zip_to(find_special_paths(os.getcwd()), args.tozip)

if __name__ == "__main__":
    main()
