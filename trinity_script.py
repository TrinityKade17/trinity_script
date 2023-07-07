#Shebang line
#!/usr/bin/env python3

#Storebought modules
import os
import re
import sys
import glob
import time
import math
import shutil
import argparse
import itertools
import subprocess
import numpy as np
import pandas as pd

#At runtime set working directory to the place where the script lives
working_dir = sys.path[0]+'/' 
os.chdir(working_dir)

#Set up an argument parser
parser = argparse.ArgumentParser(description='Script for moving files based on a list input')

parser.add_argument('-s', '--source_dir', type=int, metavar='', required=True, help='This should be a full path to the directory where the full pool of proteome files lives')
parser.add_argument('-l','--list_file', type=int, metavar='', metavar=True, help='This should be a text file containing the name of each file to copy, with each file on a new line')
parser.add_argument('-d','--dest_dir', type=str, metavar='', required=True, help='This should be a full path to the directory where you would like these to land; the scipt will create this folder if needed')

#Define the parser
args = parser.parse_args

#Store arguments
source_dir=args.source_dir
list_file=args.list_file
dest_dir=args.dest_dir

#Read in list file
list_df=read_table(file=list_file)

#For loop start
for f in list_df:
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    else:
        print("dest_dir already exists. Writing files to existing directory")
    print("Copying file:"+str(l))
    shutil.copy2(source_dir+str(l), dest_dir)
