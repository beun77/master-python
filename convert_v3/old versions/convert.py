# -*- coding : utf-8 -*-

# We import every useful library

import os, sys, time
from PIL import Image


# We initiate our launching options

FAST = False
HELP = False
REPLACE = False
ZIP = False
RECURSIVE = False
PREFIX = False
SUFFIX = False

# We analyze and update our launching options

if len(sys.argv)>= 2 :

	if sys.argv[1][0] == "-" :
		for elt in sys.argv[1] :
			if elt == "f" :
				FAST = True
			elif elt == "h" :
				HELP = True
			elif elt == "r" :
				REPLACE = True
			elif elt == "z" :
				ZIP = True
			elif elt == "R" :
				RECURSIVE = True
			elif elt == "s" :
				SUFFIX = True
			elif elt == "p" :
				PREFIX = True
			elif elt != "-" :
				print("Invalid option\n")
				sys.exit(0)
	else :
		print("Invalid option\n")
		sys.exit(0)



if HELP == True :
	print("\n\n"+open("READ_ME.txt",'r').read()+"\n")
	sys.exit(0)

if REPLACE == True :
	print("Sorry, the 'replace'  option is not available yet")
if ZIP == True :
	print("Sorry, the 'zip' option is not available yet")
if RECURSIVE == True :
	print("Sorry, the 'recursive' option is not available yet")
s = str()
if SUFFIX == True :
	s=str(raw_input("Enter a suffix for your files"))
p = str() 
if PREFIX == True :
	p=str(raw_input("Enter a prefix for your files"))




# We start our main program

list_ = open("list.txt",'r')
List = list_.read().split("\n")

List2 = list()

flist = ["jpg","png","bmp","gif","tiff"]
Flist = ", ".join(flist)


# We ask the user about his desired final format

F = "NC"

while F == "NC" :
	G = str(raw_input("Enter the final format of your pictures among "+Flist+"\n"))
	for elt in flist :
		if G == elt :
			F = G
			break
		else :
			F = "NC"


# We analyze the files to convert

sys.stdout.write("\nAnalyzing the files...")

folder = os.getcwd()

k = 0
for elt in folder :
	k+=1
print(folder)
total = 0

for elt in List :
	l = 0
	for el in elt :
		l+=1
	if l != 0 :
		List2.append(elt[k+1:])
		total+=1

if FAST == False :
	time.sleep(1)
sys.stdout.write("\rFiles analyzed \n")

# Finally, we convert the files

current = 0

for elt in List2 :
	j = 0
	k = 0
	for el in elt :
		if el == "." :
			break
		else :
			j+=1
		k +=1

	name = elt[:j]
	sys.stdout.write('\n'+"Opening "+elt+"...")
	pic = Image.open(elt)

	if FAST == False :
		time.sleep(0.6)

	sys.stdout.write('\r' + ' '*(k+15))
	sys.stdout.write('\r' + "Opened " + elt + "\n")

	name2 = s + name + p + "." + F
	sys.stdout.write('\r'+"Saving "+name2+"...")
	pic.save(name2)

	current+=1
	percentage = int(100*current/total)
	prog = int(percentage/10 +1)
	progression = "["+"#"*prog+"-"*(10-prog)+"]"
	"""
	if percentage <= 10 :
		progression = "[#---------]"
	elif percentage <= 20 :
		progression = "[##--------]"
	elif percentage <= 30 :
		progression = "[###-------]"
	elif percentage <= 40 :
		progression = "[####------]"
	elif percentage <= 50 :
		progression = "[#####-----]"
	elif percentage <= 60 :
		progression = "[######----]"
	elif percentage <= 70 :
		progression = "[#######---]"
	elif percentage <= 80 :
		progression = "[########--]"
	elif percentage <= 90 :
		progression = "[#########-]"
	elif percentage <= 100 :
		progression = "[##########]"
	"""
	sys.stdout.write('\r' + ' '*(j+14))
	sys.stdout.write('\r' + "Saved " + name2 + " "*(60-j-14) + progression + "  " + str(percentage) + "%\n")
	

list_.close()

print("\nDone \n")
