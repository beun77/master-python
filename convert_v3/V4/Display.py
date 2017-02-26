
def display(string,over,Len):   # Allows compatibility with Python 2 and, more importantly, simplifies the dynamic print
	if over == "over":
		sys.stdout.write("\r"+string+" "*(Len+1-len(string)))
		sys.stdout.flush()
	else :
		sys.stdout.write("\r"+string)
		sys.stdout.flush()
	return


def Display(string,X,Y) :   # This prints a given string at the specified position according to its coordonates (X,Y)
	curses.noecho()
	curses.cbreak()
	if X < 0 or X >= curses.COLS :
		X = 0
	if Y < 0 or Y >= curses.LINES :
		Y = 0	
	#Xmax = Xmin+curses.COLS-1
	#Ymax = Ymin+curses.LINES-1
	addstr(Y,X,string)
	return


def nav(enable, file) :
	Fl = open(file,'r')
	F = FL.read().split("<new>")
	Ymin = F.len()-curses.LINES
	while enable == 1 :
		# Displays elements written before or after the current displayed ones according to the hitten arrow key
		stdscr.keypad(True)
		key = stdscr.getkey()
		X = 10
		Y = 30

		if key == "KEY_UP" :
			Ymin += 3
		elif key == "KEY_DOWN" :
			Ymin -= 3

		to_display = F[Ymin:Ymax]
		Display("\n".join(to_display), X, Y)
		Fl.close()
	return


def store(string, file) :
	# Stores all relevant informations in a text file => Helps in case of error or just to use the nav function
	Fl = open(file,'a+')
	Fl.write(string+"<new>", 'a')
	Fl.close()
	return

def progression(current,total):     # This is just about calculating and displaying the progression of the conversion or the compression
	
	percentage = int(100*current/total)
	prog = int(percentage/5 +1)
	progression = "["+"#"*prog+"-"*(20-prog)+"]"
	
	return [progression, percentage]

