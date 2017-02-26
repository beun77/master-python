
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

