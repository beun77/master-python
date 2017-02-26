# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##


import read_file,display,error,os

def coach(music,mode,ref_table) : # Decides of the following events according to the difficulties of the player

	if mode == 'basic' : # Just waits for the player to press the right keys in order to generate the animation of the next 2 seconds
		fsampling,Notes = read_file.read_tlp(music)
	
		for sample in Notes :
			display.disp(Notes[sample],fsampling) # The current structure of dis does not allow this contruction...
			error = error.get_error()

	elif mode == 'none' : # Just displays the notes, regardless of the player's performance

		Notes,fsampling = read_file.read(music)
		display.disp(Notes,fsampling,100,ref_table)

	else :
		print("Unavailable function at the moment")


	return exit_flag # The player needs to be able to quit the software at any moment

