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

def Help(state) :

	if state == "idle" :
		string = open('READ_ME.txt','r').read()
	elif state == "format" :
		string = "This software converts pictures from a format in another format. Possible formats currently are "+Flist+". For instance if you want your files to be converted in jpg, simply type 'jpg'."
	elif state == "prefix" :
		string = "A prefix is a small string that is written at the beginning of the files' name. For instance, if you type 'converted_', all your converted files will be named 'converted_X' where X is their original name."
	elif state == "suffix" :
		string = "A suffix is a small string that is written at the end of the files' name. For instance, if you type '_converted', all your converted files will be named 'X_converted' where X is their original name."
	elif state == "compress" :
		string = "You have selected the compress option. This will compress all your converted pictures in a 7z or a tar.gz file of which name can be set. For instance, if you type 'compressed', your archive will be named 'compressed'."
	elif state == "decompress" :
		string = "An archive has been found in analyzed folder. You can choose to decompress it and convert all pictures that could be stored in it, or you can choose to ignore it."
	elif state == "remove" :
		string = "You have selected the replace option. This will replace all original files by the converted files. This means that all original files will be deleted with no back-up possibility! Think about it carefully, especially if you have selected a final format with loss as jpg."
	elif state == "resize" :
		string = "In order to resize your pictures, you have to enter their final dimensions. This must be set using this format of instruction: 'WxH u' where W is the width, H is the height and u is the unit. Two units are available: 'asm' and 'osr'. The first one is an absolute unit expressed in pixels and the second one is a relative unit expressed as a percentage. If W or H is left at 0, it will automatically be set according to the original ratio.\nFor instance, if you type 100x200 asm, all converted files will be 100 pixels wide and 200 pixels tall. If you type 100x200 osr, all converted files will be 100% their orignal wideness and 200% their original heightness. Finally, if you type 50x0 osr, all converted files will be half smaller than the original size while keeping the same ratio."
	elif state == "Memory_Warning" :
		string = "You are about to generate at least a picture of which size is superior to 30Mpix. This might induce some memory issue and a longer execution time. You can choose to continue or to ignore this files."
	else :
		string = open('READ_ME.txt','r').read()

	return print("\n\n"+string+"\n\n")


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

		PATH = False
		if len(sys.argv) >= 3 :
			if re.search(r"^/(\w/)*$",sys.argv[2]) :
				PATH = True
			else :
				print("Invalid path\n")
				sys.exit(0)


	# We act accordingly

	if HELP == True :
		Help("idle")
		sys.exit(0)

	if REPLACE == True :
		sure = "Warning"
		while sure == "Warning":
			sure = get_clean(input_("Are you sure you want to replace your files? (y/n) - h (help) q (quit)\n"))
			if sure == "n" :
				REPLACE = False
			elif sure  == "h" :
				Help(replace)
				sure = "Warning"
			elif sure == "q" :
				sys.exit(0)
			elif sure != "y" :
				sure = "Warning"
	s = str()
	if SUFFIX == True :
		tmp = "Warning"
		while tmp == "Warning":
			tmp = get_clean(str(input_("Enter a suffix for your files (15 characters max) - h (help) q (quit)\n")))
			if tmp == "q" :
				sys.exit(0)
			elif tmp == "h" :
				Help("suffix")
				tmp = "Warning"
		s = tmp
	p = str() 
	if PREFIX == True :
		tmp = "Warning"
		while tmp == "Warning":
			tmp = get_clean(str(input_("Enter a prefix for your files (15 characters max) - h (help) q (quit)\n")))
			if tmp == "q" :
				sys.exit(0)
			elif tmp == "h" :
				Help("prefix")
				tmp = "Warning"
		p = tmp

	a = str()
	if TAR == True or ZIP == True :
		tmp = "Warning"
		while tmp == "Warning":
			if TAR == True and ZIP == True :
				tmp = get_clean(str(input_("\nEnter a name for your compressed folders (15 characters max)\n")))
			else :
				tmp = get_clean(str(input_("\nEnter a name for your compressed folder (15 characters max)\n")))
			if tmp == "q" :
				sys.exit(0)
			elif tmp == "h" :
				Help("compress")
				tmp = "Warning"
		a = tmp

	size = list() 
	if RESIZE == True :
		# The user should have the choice between a relative and an absolute resize method. This can easily be done by adding virtual units. The relative unit will be "osr" for "original size relative" and the absolute unit will be "asm" for absolute size measurement. The expected input is something of the form NxM u with N the x value, M the y value and u the unit. If u is osr, x and y must be integers between 0 and 10,000 (this will be treated as a percentage), if u is asm, x and y must be integers between 0 and 100*their_original_value. If the final definition is superior to 30 Mpx, a warning message should pop.
		tmp = "Warning"
		while tmp == "Warning" :
			tmp = get_clean(input_("Enter a new size for your converted pictures. Input format must be WxH u where W is the width, H is the height and u is the unit.\nTwo units currently exists: osr is a relative unit - 100 osr corresponds to the original size - and asm is an absolute unit - 100 asm corresponds to a 100 pixels. If W or H equals zero, it will be set according to the original ratio.\n"))
			if re.search(r"^[0-9]{1,8}x[0-9]{1,8}\s(asm|osr)$",tmp) :
				size = tmp
			elif tmp == "h" :
				Help("resize")
				tmp == "Warning"
			elif tmp == "q" :
				sys.exit(0)
			else :
				tmp = "Warning"

		l = size.split(" ")
		m = l[0].split("x")
		W = int(m[0])
		H = int(m[1])

		size = [W,H,l[1]]
	
	options = [FAST, HELP, REPLACE, ZIP, RECURSIVE, PREFIX, SUFFIX, RESIZE, TAR, PATH, p, s, a, size]

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
						tmp = get_clean(str(input_("\nA compressed file has been found. Do you want to decompress it? (y/n) - h (help) q (quit)\n")))
						if tmp == "y" or tmp == "n" :
							break
						elif tmp == "h" :
							Help("decompress")
						elif tmp == "q" :
							sys.exit(0)
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
			if tmp != "y" and tmp != "n" and tmp != "h" and tmp != "q":
				tmp = "Warning"
			elif tmp == "n" :
				return sys.exit(0)
			elif tmp == "h" :
				Help("Memory_warning")
				tmp = "Warning"
			elif tmp == "q" :
				sys.exit(0)

	return [w,h,size[2]]



def get_format():   # This gets the final format the user wants his pictures to be converted to

	F = "NC"
	filesname = list()


	Flist = ", ".join(flist)

	while F == "NC" :
		G = get_clean(str(input_("\nEnter the final format of your pictures among "+Flist+" - h (help) q (quit)\n")))
		for elt in flist :
			if G == elt :
				F = G
				break
			else :
				if G == "h" :
					Help('format')
					F = "NC"
				elif G == "q" :
					sys.exit(0)
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

def resize(img, size):   # This rsizes an image to a given size according to the dimensions or the scale entered by the user
	W = size[0]
	H = size[1]
	if W == 0 :
		if H == 0 :
			W = img.size[0]
			H = img.size[1]
		else :
			W = int(H*img.size[0]/img.size[1])
	if H == 0 :
		if W != 0 :
			H = int(W*img.size[1]/img.size[0])
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
else :
	folder = os.getcwd()

analyze_data("original", filesname, filespath, RECURSIVE)

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
