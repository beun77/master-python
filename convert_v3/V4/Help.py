
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

	return print("\n\n"+"#"*50+"\n\nHELP\n\n"+string+"\n\n"+"#"*50+"\n\n")

