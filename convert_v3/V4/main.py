# -*- coding : utf-8 -*-

# We import every useful library

import os, sys, time, re, tarfile
from PIL import Image
from os.path import isfile, join
import curses

import Convert, Analyze, Options, Help, Display 

#stdscr = curses.initscr()
version = "v3.4.1"




# We start our main program

greetings(version)


# First, we initialize our global variables


flist = ["jpg","png","bmp","gif","tiff","pdf"]

options = get_options()

FAST = options[0]
HELP = options[1]
REPLACE = options[2]
ZIP = options[3]
RECURSIVE = options[4]
PREFIX = options[5]
SUFFIX = options[6]
RESIZE = options[7]
TAR = options[8]
PATH = options[9]
p = options[10]
s = options[11]
a = options[12]
size = options[13]

# We ask the user about his desired final format

F = get_format()


# We analyze the files to convert

display("\nAnalyzing the files...","notover",0)

Decompressed = list()
filespath = list()
filesname = list()

if PATH == True :
	folder = sys.argv[2]
	fld = ""
else :
	folder = os.getcwd()
	fld = "original"

analyze_data(fld, filesname, filespath, RECURSIVE)

if RESIZE == True :   
	size = memory_warning(size, filesname, filespath)


total = 0
for elt in filesname:
	total+=1

if FAST == False :
	time.sleep(1)
display("Files analyzed:","over",30)
print("\n"+", ".join(filesname))

# Finally, we convert the files

max1 = 0
max2 = 0

for elt in filesname :
	if len(elt) > max1:
		max1 = len(elt)
for elt in filespath :
	if len(elt) > max2:
		max2 = len(elt)

# And we compress them if needed

convertedfiles = convert(filesname, filespath, size)

if ZIP == True or TAR == True :
	print("\n\n\nCompressing files...\n")
	if FAST == False :
		time.sleep(1)
	compress(convertedfiles)

print("\n\nDone \n")

sys.exit()
