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
	Nlist = ceil(len(Samples)*fmax/fsampling) # /!\ The FFT could be faster if it was calculated on 2**n samples for symetry reasons
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



def homogenize(frames,ref_table) :
	# We eliminate all notes that are not present in more than 3 samples in a row (we consider them as too short to not be a calculation error)

	frames_copy = dict(frames) # frames is a dictionary containing lists of notes (ie lists of a position and a magnitude)
	for note in ref_table :
		num_sample = list()
		for frame in frames_copy : # We start by looking at which samples contains this note
			for f in frames_copy[frame] :
				if note == f[0] :
					num_sample.append(frame)
		if len(num_sample) > 3 :
			count_is = 0 # Number of samples containing the note
			count_isnt = 0 # Number of samples not containing the note
			to_delete_from = list() # List of samples from which the note should be deleted
			i = 0
			while i < len(num_sample) :
				# /!\ What if we have something like : num_sample = [1,2,3,5,6,7] ? This note will totally be removed even though it lasts about a third of a second
				# The idea is to eliminate every note that is present in less than 5 samples out of 8 in a row
				to_delete_from.append(num_sample[i])
				if i == len(num_sample)-1 : # There is some side effects when processing the last non empty sample
					tmp = num_sample[i]-num_sample[i-1]
				else :
					tmp = num_sample[i+1]-num_sample[i]
				if tmp > 0 :
					if tmp == 1 : # The samples are consecutives
						count_is += 1
					else :
						count_isnt += tmp-1
				if count_is + count_isnt >= 8 :
					if count_is <= 5 : # This note is to be eliminated from those samples
						for s in to_delete_from :
							pos = 0
							for n in frames_copy[s] :
								if n[0] == note :
									del frames[s][pos]
								pos += 1
					else : # This note is to stay in those samples
						to_delete_from = list()
					count_is = 0
					count_isnt = 0
				i+=1

	return frames


def analyze(music,ref_table) : #Analyzes a music (mp3 file in a folder)
	analysis = str()
	#print("Unavailable function at the moment")
	f = open(music[:len(music)-3]+'tlp','w')
	Samples,fsampling,read = read_file.read_music(music) # We start by reading the mp3 file

	if read :
		SAMPLES = split(Samples,fsampling,20) # Then we split it
		#analysis+="f"+str(fsampling)+"\n" # f stands for the sampling frequency
		#analysis+="<start>"
		frames = dict()
		for sample in SAMPLES : # And we analyze the notes and their intensity in each portion of the piece
			#analysis+="\ns" # s stands for sample
			fft = analyze_notes.FFT(SAMPLES[sample],fsampling)
			#Notes = analyze_notes.which_note(fft,ref_table)
			Notes = analyze_notes.which_note2(fft,ref_table) # which_note2 seems to work better, even though it is not perfect
			frames[sample] = []
			for note in Notes :
				frames[sample] += [[note[0],note[1]]]
				#analysis+="p"+str(note[0])+"m"+str(note[1]) # p stands for position, m stands for magnitude
		#analysis+="\n<end>"
		#analysis = "\ns".join([header]+samples) # Finally we reconstitute our analysis
		#analysis = "\n".join([analysis]+[footer])

		frames = homogenize(frames,ref_table)
		frames_list = list()
		analysis = "f"+str(fsampling)+"\n<start>"
		for frame in frames :
			analysis += "\ns"
			for note in frames[frame] :
				analysis += str(note[0])+";"+str(note[1])+"|"
		analysis += "\n<end>"
		# Then we also need to analyze the fingering
		f.write(analysis)
		f.close()
		return

	else :
		print("This file "+music+" could not be read. Analyze aborted.")
		return
