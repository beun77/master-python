# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##

import read_file, listen, analyze_notes, analyze_music, error, coach, display
import os
from os.path import isfile, join
# Analyze_notes will not be used here in the future as it will be directly called by analyze_music and by error; write_file will also be directly called by analyze_music



def select(string) : #Selects an item (song to play, coaching mode, etc) - 2 buttons to choose, 1 to confirm + 1 to quit the soft

	print("Unavailable function at the moment")

	print(string)

	# Needs to display the name of the song somewhere (console or B&W screen via display.screen_disp())
	
	selected = 'exit'

	return selected


def analyze(folder,ref_table) : # Analyzes a given folder
	print("Looking for new files...")
	files = list()
	f = open(str(os.getcwd())+'/files.tlp','r+')
	files_list = f.read().split("\n")
	f.close()
	f = open(str(os.getcwd())+'/files.tlp','a+')
	for File in os.listdir(folder):
		if isfile(folder+File):   # This select all files in the folder
			if File.endswith(".mp3") : # At the moment, only mp3 files are supported, but more is to come
					files.append(File)
	for elt in files :
		already_analyzed = False
		for el in files_list :
			if el == elt :
				already_analyzed = True
		if not already_analyzed :
			print("Analyzing "+elt+"...")
			analyze_music.analyze(folder+elt,ref_table)
			f.write(elt+'\n')
			print(elt+" analyzed")
	print("All files have been analyzed")
	f.close()
	return


def __main__() : # Main programm of The Ligh Piano system

	display.greetings()

	ref_table = analyze_notes.piano_keyboard(88)
	print(ref_table)
	"""
	Samples,fsampling = read_file.read_test()
	#print(Samples)
	SAMPLES = analyze_notes.split(Samples,fsampling,200)
	#print(SAMPLES)

	for sample in SAMPLES :
		fft = analyze_notes.FFT(SAMPLES[sample],fsampling)
		#print(fft)	
		Notes = analyze_notes.which_note(fft,ref_table)
		print('Notes',Notes)
	"""
	
	folder = os.getcwd()+"/music/"
	analyze(folder,ref_table) # First we strat by analyzing any new piece of music

	exit_flag = False

	while not exit_flag :

		music = select('Select the piece of music you would like to work on.')

		if music == 'exit' :
			exit_flag = True
			break
		else :
			exit_flag = coach.coach(music) # Finally we read it and launch the coach option

	display.see_you()

	return


__main__()

