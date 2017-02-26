
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
					filesname = list()		# PROBLEM WITH RECURSIVITY ? IT DECOMPRESSES THE FOLDER BUT DOES NOT ANALYZE IT 
					filespath = list()
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

