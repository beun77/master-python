# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##

import analyze_notes, read_file
from math import ceil


def fingering(Notes,HandSize) : # Calculates the optimum fingering given the Notes (text file containing the notes with the reading frequency in the header) according to the HandSize (maximum distance covered by the spreaded hand of the player) - Writes in the same file

	print("Unavailable function at the moment")

	return


def split(Samples,fsampling,fmax) : # Splits a list of Samples into a dictionary of shorter list of samples
	# fsampling is the sampling frequency and fmax is the maximum characteristic frequency for the splitting process
	D = dict()
	tau = 1/fsampling
	Tmax = 1/fmax
	k = 0
	Nlist = ceil(len(Samples)*fmax/fsampling) # /!\ THE FFT COULD BE FASTER IF IT WAS CALCULATED ON 2**n SAMPLES
	#Nsamples = ceil(len(Samples)/Nlist)
	counter = 0
	while k < Nlist : # While there is still some clustering to do
		T = 0
		tmp = list()
		i = 0
		while T < Tmax and counter < len(Samples) : # We build a shorter list
			T += tau
			#tmp.append(Samples[k*Nsamples+i])
			tmp.append(Samples[counter])
			counter += 1
			i += 1
		D[k] = tmp
		k += 1
	return D



def analyze(music,ref_table) : #Analyzes a music (mp3 file in a folder)
	analysis = str()
	#print("Unavailable function at the moment")
	f = open(music[:len(music)-3]+'tlp','w')
	Samples,fsampling,read = read_file.read_music(music) # We start by reading the mp3 file
	if read :
		SAMPLES = split(Samples,fsampling,50) # Then we split it
		analysis+="f"+str(fsampling)+"\n" # f stands for the sampling frequency
		analysis+="<start>\n"
		for sample in SAMPLES : # And we analyze the notes and their intensity in each portion of the piece
			analysis+="s\n" # s stands for sample
			fft = analyze_notes.FFT(SAMPLES[sample],fsampling)
			Notes = analyze_notes.which_note(fft,ref_table)
			for note in Notes :
				analysis+="p"+str(note[0])+"m"+str(note[1]) # p stands for position, m stands for magnitude
		analysis+="\n<end>"
		# Then we also need to analyze the fingering
		f.write(analysis)
		f.close()
		return

	else :
		print("This file "+music+" could not be read. Analyze aborted.")
		return
