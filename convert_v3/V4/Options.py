
def input_(string):      # Allows compatibility with Python 2
	if sys.version_info[0] < 3 :
		return raw_input(string)
	else :
		return input(string)



def get_clean(string):  # Helps to fight against any code injection attack
	if re.search(r"^[0-9A-Za-z-_ ]{1,15}$", string) is None :
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
		tmp = "Warning"
		while tmp == "Warning" :
			tmp = get_clean(input_("Enter a new size for your converted pictures. Input format must be WxH u where W is the width, H is the height and u is the unit.\nTwo units currently exists: osr is a relative unit - 100 osr corresponds to the original size - and asm is an absolute unit - 100 asm corresponds to a 100 pixels. If W or H equals zero, it will be set according to the original ratio. - h (help) q (quit)\n"))
			if not (re.search(r"^[0-9]{1,8}x[0-9]{1,8} (asm|osr)$",tmp) is None) :
				size = tmp
			elif tmp == "h" :
				Help("resize")
				tmp = "Warning"
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


