# -*- coding : utf-8 -*-

import os, sys, time
from PIL import Image

list_ = open("list.txt",'r')
List = list_.read().split("\n")

List2 = list()

flist = ["jpg","png","bmp"]
"""
f = "NC"

while f == "NC" :
	g = str(input("Enter the original format of your pictures among " + ", ".join(flist) +" \n"))
	for elt in flist :
		if g == elt :
			f = g
			break
		else :
			f = "NC"
"""

F = "NC"

while F == "NC" :
	G = str(input("Enter the final format of your pictures among " + ", ".join(flist) +" \n"))
	for elt in flist :
		if G == elt :
			F = G
			break
		else :
			F = "NC"


print("\nAnalyzing the files...")

folder = os.getcwd()

k = 0
for elt in folder :
	k+=1

total = 0

for elt in List :
	l = 0
	for el in elt :
		l+=1
	if l != 0 :
		List2.append(elt[k+1:])
		total+=1

sys.stdout.flush()
print("Files analyzed \n")

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

	time.sleep(0.6)
	sys.stdout.write('\r' + ' '*(k+15))
	sys.stdout.write('\r' + "Opened " + elt + "\n")

	name2 = name + "." + F
	sys.stdout.write('\r'+"Saving "+name2+"...")
	pic.save(name2)

	current+=1
	percentage = int(100*current/total)
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

	sys.stdout.write('\r' + ' '*(j+14))
	sys.stdout.write('\r' + "Saved " + name2 + " "*(60-j-14) + progression + "  " + str(percentage) + "%\n")
	

list_.close()

print("\nDone \n")
