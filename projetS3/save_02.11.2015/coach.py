# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##


import read_file,display,error,os

def coach(music,mode) : # Decides of the following events according to the difficulties of the player

	if mode == 'basic' : # Just waits for the player to press the right keys in order to generate the animation of the next 2 seconds
		fsampling,Notes = read_file.read_tlp(music)
		tau = 1/fsampling
		t = 0

		for sample in Notes :
			# Pause of a tau length
			t += tau
			display.disp(sample)
			error = error.get() # We check if the player has made an error or not
			
			


	else :
		print("Unavailable function at the moment")


	return exit_flag # The player needs to be able to quit the software at any moment

