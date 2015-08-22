# -*- coding : utf-8 -*-

# We import every useful library

import os, sys, time, re
from PIL import Image
from os.path import isfile, join

def input_(string):
	if sys.version_info[0] < 3 :
		return raw_input(string)
	else :
		return input(string)



def get_clean(string):  # Helps to fight against any code injection attack
	if re.search(r"^[0-9A-Za-z-_]*?$", string) is None :
		return "Warning"
	else :
		return string



def get_options():

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



	# We act accordingly

	if HELP == True :
		print("\n\n"+open("READ_ME.txt",'r').read()+"\n")
		sys.exit(0)

	if ZIP == True :
		print("Sorry, the 'zip' option is not available yet")
	if REPLACE == True :
		sure = "Warning"
		while sure == "Warning":
			sure = get_clean(input_("Are you sure you want to replace your files ? (yes/no)\n"))
			if sure == "no" :
				REPLACE = False
			elif sure != "yes" :
				sure = "Warning"
	s = str()
	if SUFFIX == True :
		tmp = "Warning"
		while tmp == "Warning":
			tmp = get_clean(str(input_("Enter a suffix for your files (15 characters max)\n")))
		s = tmp
	p = str() 
	if PREFIX == True :
		tmp = "Warning"
		while tmp == "Warning":
			tmp = get_clean(str(input_("Enter a prefix for your files (15 characters max)\n")))
		p = tmp

	options = [FAST, HELP, REPLACE, ZIP, RECURSIVE, PREFIX, SUFFIX, p, s]

	return options


def analyze_data(Dir, List2, List3, k):
	for File in os.listdir(folder+"/"+Dir):

		if isfile(folder+"/"+Dir+"/"+File):
			for f in flist :
				if File.endswith("."+f):
					List2.append(File)
					List3.append(folder+"/"+Dir)
		elif RECURSIVE == True:
			analyze_data(Dir+"/"+File, List2, List3, k)

	return 


def get_format():

	F = "NC"
	List2 = list()


	Flist = ", ".join(flist)

	while F == "NC" :
		G = str(input_("Enter the final format of your pictures among "+Flist+"\n"))
		for elt in flist :
			if G == elt :
				F = G
				break
			else :
				F = "NC"

	return F


def progression(current,total):
	
	percentage = int(100*current/total)
	prog = int(percentage/10 +1)
	progression = "["+"#"*prog+"-"*(10-prog)+"]"
	
	return [progression, percentage]


def convert(List2, List3):
	current = 0

	l = 0

	for elt in List2 :
		j = 0
		for el in elt :
			if el == "." :
				break
			else :
				j+=1

		Dir1 = List3[l]
		Dir2 = Dir1.split("/")
		n = 0
		for el in Dir2 :
			if el == "original":
				Dir2[n] = "converted"
				break
			n+=1
		Dir2 = "/".join(Dir2)
		l+=1

		name = elt[:j]
		sys.stdout.write('\n'+"Opening "+Dir1+"/"+elt+"...")
		pic = Image.open(Dir1+'/'+elt)

		if FAST == False :
			time.sleep(0.8)

		k=0
		for lett in Dir1 :
			k+=1
		K=0
		for lett in Dir2 :
			K+=1
		sys.stdout.write('\r' + ' '*(k+j+15))
		sys.stdout.write('\r' + "Opened " +Dir1+'/'+ elt + "\n")

		name2 = s + name + p + "." + F

		if os.path.exists(Dir2) == False :
			os.mkdir(Dir2)

		sys.stdout.write('\r'+"Saving "+Dir2+"/"+name2+"...")
		pic.save(Dir2+'/'+name2)

		current+=1
		sys.stdout.write('\r' + ' '*(K+j+14))
		Prog = progression(current, total)
		Progression = Prog[0]
		Percentage = Prog[1]
		sys.stdout.write('\r' + "Saved " + Dir2+"/"+name2)
		sys.stdout.write( " "*(60-K-j-14) + Progression + "  " + str(Percentage) + "%\n")
		if REPLACE == True :
			os.remove(Dir1 + '/' + elt)

	return

# We start our main program
flist = ["jpg","png","bmp","gif","tiff","pdf"]
options = get_options()
FAST = options[0]
HELP = options[1]
REPLACE = options[2]
ZIP = options[3]
RECURSIVE = options[4]
PREFIX = options[5]
SUFFIX = options[6]
p = options[7]
s = options[8]

# We ask the user about his desired final format

F = get_format()

# We analyze the files to convert

sys.stdout.write("\nAnalyzing the files...")

List3 = list()
List2 = list()
k = 0
folder = os.getcwd()
for elt in folder :
	k+=1

analyze_data("original", List2, List3, k)

total = 0
for elt in List2:
	total+=1

if FAST == False :
	time.sleep(1)
sys.stdout.write("\rFiles analyzed         \n")
print(List2)

# Finally, we convert the files

convert(List2, List3)

print("\nDone \n")
