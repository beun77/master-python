# -*- coding : utf-8 -*-

# We import every useful library

import os, sys, time, re, tarfile
from PIL import Image
from os.path import isfile, join



version = "v3.4.1"


def greetings(version) :
	a = int((25-len(version))/2)
	b = 25-len(version)-a
	print("\n\n"+"#"*29+"\n##"+" "*25+"##\n##    C O N V E R T E R    ##\n##"+" "*a+version+" "*b+"##\n##"+" "*25+"##\n"+"#"*29+"\n\nThank you for trying this software. I hope you like it.\n\n\n")
	return



def display(string,over,Len):   # Allows compatibility with Python 2 and, more importantly, simplifies the dynamic print
	if over == "over":
		sys.stdout.write("\r"+string+" "*(Len+1-len(string)))
		sys.stdout.flush()
	else :
		sys.stdout.write("\r"+string)
		sys.stdout.flush()
	return


def input_(string):      # Allows compatibility with Python 2
	if sys.version_info[0] < 3 :
		return raw_input(string)
	else :
		return input(string)



def get_clean(string):  # Helps to fight against any code injection attack
	if re.search(r"^[0-9A-Za-z-_]{1,15}$", string) is None :
		return "Warning"
	else :
		return string



def get_options():    # This analyse any possible launching options

	# We initiate our launching options

	FAST = False
	HELP = False
	REPLACE = False
	ZIP = False
	RECURSIVE = False
	PREFIX = False
	SUFFIX = False
	RESIZE = False
	TAR = False

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
				elif elt == "t":
					TAR = True
				elif elt == "S" :
					RESIZE = True
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

	if REPLACE == True :
		sure = "Warning"
		while sure == "Warning":
			sure = get_clean(input_("Are you sure you want to replace your files? (y/n)\n"))
			if sure == "n" :
				REPLACE = False
			elif sure != "y" :
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

	a = str()
	if TAR == True or ZIP == True :
		tmp = "Warning"
		while tmp == "Warning":
			if TAR == True and ZIP == True :
				tmp = get_clean(str(input_("\nEnter a name for your compressed folders (15 characters max)\n")))
			else :
				tmp = get_clean(str(input_("\nEnter a name for your compressed folder (15 characters max)\n")))
		a = tmp

	size = list() 
	if RESIZE == True :
		# The user should have the choice between a relative and an absolute resize method. This can easily be done by adding virtual units. The relative unit will be "osr" for "original size relative" and the absolute unit will be "asm" for absolute size measurement. The expected input is something of the form NxM u with N the x value, M the y value and u the unit. If u is osr, x and y must be integers between 0 and 10,000 (this will be treated as a percentage), if u is asm, x and y must be integers between 0 and 100*their_original_value. If the final definition is superior to 30 Mpx, a warning message should pop.
		tmp = "Warning"
		while tmp == "Warning" :
			tmp = get_clean(input_("Enter a new size for your converted pictures. Input format must be WxH u where W is the width, H is the height and u is the unit.\nTwo units currently exists: osr is a relative unit - 100 osr corresponds to the original size - and asm is an absolut unit - 100 asm corresponds to a 100 pixels -\n"))
			if re.search(r"^[0-9]{1,8}[x]{1}[0-9]{1,8}[asm]{1}$",tmp) or re.search(r"^[0-9]{1,8}[x]{1}[0-9]{1,8}['osr']{1}$",tmp) :
				size = tmp
			else :
				tmp = "Warning"

		l = size.split(" ")
		m = l[0].split("x")
		W = int(m[0])
		H = int(m[1])

		size = [W,H,l[1]]
	
	options = [FAST, HELP, REPLACE, ZIP, RECURSIVE, PREFIX, SUFFIX, RESIZE, TAR, p, s, a, size]

	return options


def analyze_data(Dir, filesname, filespath, RECURSIVE):      # This analyze the "original" folder

	folders = list()

	for File in os.listdir(folder+"/"+Dir):
		
		if isfile(folder+"/"+Dir+"/"+File):   # This select all files in the folder
			compatible = False
			for f in flist :    # We verify if this file is a picture of the right format
				if File.endswith("."+f) and f!="pdf":
					filesname.append(File)
					filespath.append(folder+"/"+Dir)
					compatible = True
					
			if tarfile.is_tarfile(folder+"/"+Dir+"/"+File) and compatible == False:    # Or if it is an archive of the right format
				Dcmprssd = False
				for D in Decompressed :
					if folder+"/"+Dir+"/"+File == D:
						Dcmprssd = True
				rep = "no" 
				if Dcmprssd == False :    # If it is an archive and if it has not been decompressed yet, we ask the user what he wants to do
					tmp = "Warning"
					while tmp == "Warning" :
						tmp = get_clean(str(input_("\nA compressed file has been found. Do you want to decompress it? (y/n)\n")))
						if tmp == "y" or tmp == "n" :
							break

						else :
							tmp = "Warning"
					rep = tmp

				if rep == "y":  # And we act accordingly
					tar = tarfile.open(folder+"/"+Dir+"/"+File)
					tar.extractall(folder+"/"+Dir)
					tar.close()
					Decompressed.append(folder+"/"+Dir+"/"+File)
					#filesname = list() 
					#filespath = list()
					RECURSIVE = True
					analyze_data(Dir, filesname, filespath, RECURSIVE)
		elif RECURSIVE == True:
			folders.append(File)

	if RECURSIVE == True:
		for Folder in folders :
			analyze_data(Dir+"/"+Folder, filesname, filespath, RECURSIVE)

	return 



def memory_warning(size, filesname, filespath) :
	warn_memory = False
	w = size[0]
	h = size[1]
	k = 0
	for pic in filesname :
		img = Image.open(filespath[k]+"/"+filesname[k])
		W = img.size[0]
		H = img.size[1]

		if size[2] == "osr" :
			if W > 10000 or H > 10000 :
				w = 10000
				h = 10000
			if w*W*h*H/10000 > 30000000 :
				warn_memory = True
		elif size[2] == "asm" :
			if W*H > 30000000 :
				warn_memory = True
		k+=1

	if warn_memory :
		tmp = "Warning"
		while tmp == "Warning" :
			tmp = get_clean(input_("Warning: this will produce large files and might result in memory issue. Are you sure you want to continue? (y/n)"))
			if tmp != "y" and tmp != "n" :
				tmp = "Warning"
			else :
				return sys.exit()

	return [w,h,size[2]]



def get_format():   # This gets the final format the user wants his pictures to be converted to

	F = "NC"
	filesname = list()


	Flist = ", ".join(flist)

	while F == "NC" :
		G = str(input_("\nEnter the final format of your pictures among "+Flist+"\n"))
		for elt in flist :
			if G == elt :
				F = G
				break
			else :
				F = "NC"

	return F


def progression(current,total):     # This is just about calculating and displaying the progression of the conversion or the compression
	
	percentage = int(100*current/total)
	prog = int(percentage/5 +1)
	progression = "["+"#"*prog+"-"*(20-prog)+"]"
	
	return [progression, percentage]


def make_dir(Dir):     # This creates the Dir if it does not already exists
	l = Dir.split("/")
	m = str()
	for elt in l :
		m = m+"/"+elt
		if os.path.exists(m) == False:
			os.mkdir(m)
	return

def resize(img, size):
	W = size[0]
	H = size[1]
	if size[2] == "osr" :
			W = int(img.size[0]*W/100)
			H = int(img.size[1]*H/100)
	img = img.resize((W, H), Image.ANTIALIAS)
	return img


def convert(filesname, filespath, size):   # This converts the files whose names are in filesname and folders in filespath
	current = 0

	convertedfiles = list()  # convertedfiles is the list of converted objects

	l = 0

	for elt in filesname :
		j = 0
		for el in elt :
			if el == "." :
				break
			else :
				j+=1

		Dir1 = filespath[l]
		Dir2 = Dir1.split("/")
		n = 0
		for el in Dir2 :
			if el == "original":
				Dir2[n] = "computed"
				break
			n+=1
		Dir2 = "/".join(Dir2)
		l+=1
		Prog = progression(current, total)
		Progression = Prog[0]
		Percentage = str(Prog[1])+"%"

		k=0
		for lett in Dir1 :
			k+=1

		name = elt[:j]
		print("\n")
		blank = max1 + max2 + 10
		display("Opening "+Dir1+"/"+elt+"..."+" "*(blank-k-j)+Progression+" "+Percentage,"notover",0)
		pic = Image.open(Dir1+'/'+elt)

		if RESIZE == True :
			pic = resize(pic,size)

		if FAST == False :
			time.sleep(1)
		K=0
		for lett in Dir2 :
			K+=1
		display(Dir1+'/'+ elt + " opened"+" "*(blank+4-k-j)+Progression+" "+Percentage,"over",blank+36)

		name2 = s + name + p + "." + F


		make_dir(Dir2)

		J = len(name2)
		display(Dir1+'/'+elt+" opened","over",k+j+blank+37)
		display("Saving "+Dir2+"/"+name2+"..."+" "*(blank+5-K-J)+Progression+" "+Percentage,"notover",0)
		pic.save(Dir2+'/'+name2)

		if FAST == False :
			time.sleep(0.6)

		current+=1
		Prog = progression(current, total)
		Progression = Prog[0]
		Percentage = str(Prog[1])+"%"
		display(Dir2+"/"+name2 + " saved"+" "*(blank+5-K-J)+Progression+" "+Percentage,"over",blank+40)
		display(Dir2+"/"+name2+" saved","over",blank+41)
		if REPLACE == True :
			os.remove(Dir1 + '/' + elt)
		convertedfiles.append(Dir2+"/"+name2)

	return convertedfiles


def compress(convertedfiles):    # This compresses the converted files

	current = 0

	if ZIP == True :
		zfile = tarfile.open(folder+"/computed/"+a+".ZIP",'w:7z')

	if TAR == True :
		tfile = tarfile.open(folder+"/computed/"+a+".tar.gz",'w:gz')

	i = 0
	for elt in convertedfiles :
		current+=1
		Prog = progression(current, total)
		Progression = Prog[0]
		Percentage = str(Prog[1])+"%"
		
		display("\n"+elt+" compressed"+" "*(105-len(elt))+Progression+" "+Percentage,"over",140)
		if ZIP == True :
			zfile.add(elt)
		if TAR == True :
			tfile.add(elt)
		os.remove(elt)

		if FAST == False :
			time.sleep(1)

		display(elt+" compressed","over",143)

	print("\n")

	if ZIP == True :
		zfile.close()
		print("\n"+folder+"/computed/"+a+".ZIP saved\n")

	if TAR == True :
		tfile.close()
		print("\n"+folder+"/computed/"+a+".tar.gz saved\n")

	return




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
p = options[9]
s = options[10]
a = options[11]
size = options[12]

# We ask the user about his desired final format

F = get_format()

# We analyze the files to convert

display("\nAnalyzing the files...","notover",0)

Decompressed = list()
filespath = list()
filesname = list()
folder = os.getcwd()

analyze_data("original", filesname, filespath, RECURSIVE)

if RESIZE == True :   
	size = memory_warning(size, filesname, filespath)


total = 0
for elt in filesname:
	total+=1

if FAST == False :
	time.sleep(2)
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
