# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##


from numpy import fft, array, nan
from math import ceil,sqrt
from matplotlib import pyplot as plt


def piano_keyboard(nbkeys) : # Defines the relationship between the frequency of the fundamental of the note and the position of the key on the keyboard
	table_ref = dict()
	if nbkeys == 88 :
		table_ref[1] = [28,'A/la']
		table_ref[2] = [30,'A#/sib']
		table_ref[3] = [31,'B/si']
		tmp = 31
		tmp2 = tmp
		tmp3 = tmp
		alpha = 2**(1/12)
		beta = sqrt(2)
		for i in range(0,7) :
			tmp*=alpha
			table_ref[4+i*12] = [ceil(tmp),'C/do']
			tmp*=alpha
			table_ref[5+i*12] = [ceil(tmp),'C#/reb']
			tmp*=alpha
			table_ref[6+i*12] = [ceil(tmp),'D/re']
			tmp*=alpha
			table_ref[7+i*12] = [ceil(tmp),'D#/mib']
			tmp*=alpha
			table_ref[8+i*12] = [ceil(tmp),'E/mi']
			tmp = tmp3*beta # Limits the inevitable derive in the frequency calculation
			table_ref[9+i*12] = [ceil(tmp),'F/fa']
			tmp*=alpha
			table_ref[10+i*12] = [ceil(tmp),'F#/solb']
			tmp*=alpha
			table_ref[11+i*12] = [ceil(tmp),'G/sol']
			tmp*=alpha
			table_ref[12+i*12] = [ceil(tmp),'G#/lab']
			tmp*=alpha
			table_ref[13+i*12] = [ceil(tmp),'A/la']
			tmp*=alpha
			table_ref[14+i*12] = [ceil(tmp),'A#/sib']
			tmp = 2*tmp2 # Limits the inevitable derive in the frequency calculation
			tmp2 = tmp
			tmp3 = tmp
			table_ref[15+i*12] = [ceil(tmp),'B/si']
		table_ref[88] = [4191,'C/do']

	else :
		print("Unavailable function at the moment")
		return piano_keyboard(88)
	return table_ref



def FFT(A,fsampling) : # Calculates the FFT (list of analyzed frequencies) from a list of A samples obtained with a sampling frequency of fsampling (will help generate the time component)
	F = list() # F is a list of tuples. Example: F = [{10,135},{20,10}] - The 10 Hz frequency has a magnitude of 135 out of 255 where the 20 Hz frequency has a magnitude of only 10 out of 255
	freq = list()
	N = len(A)
	if N == 0 :
		return []

	if N%2 == 0 :
		lim = ceil(N/2+1)
	else :
		lim = ceil((N+1)/2)
	for i in range(0,lim) :
		freq.append(i*fsampling/N)
	tmp = fft.rfft(array(A))
	tmp2 = list()
	for elt in tmp :
		if elt == nan :
			tmp2.append(0)
		else :
			tmp2.append(abs(elt))
	"""
	plt.figure()
	plt.plot(freq,tmp2)
	plt.show()
	"""

	MaxMagn = 0
	MinMagn = 10000000
	for elt in tmp2 :
		if elt > MaxMagn :
			MaxMagn = elt
		if elt < MinMagn :
			MinMagn = elt
	if MaxMagn - MinMagn != 0 :
		a = 255/(MaxMagn-MinMagn)
	else :
		a = 1
	b = a*MinMagn
	for i in range(0,len(freq)) :
		F.append([ceil(10*freq[i])/10,ceil(tmp2[i]*a-b)]) # We could have use tuples, but they are not guaranteed to keep the order
	return F # Sub-lists are normalized and sorted by increasing value of the associated frequency




def which_note(Frequencies, table_ref) : # Decides which note has been played thanks to a list of frequencies and their associated intensity according to the shape of the keyboard
	Notes = list()
	# We start by removing all frequencies that are too weak
	MagnMax = 0
	for f in Frequencies :
		if f[1] > MagnMax :
			MagnMax = f[1]
	Freq = list(Frequencies)
	#print(Frequencies)
	for f in Frequencies :
		if f[1] <= 15 :
			Freq.remove(f)
	#print(Freq)
	# Then, we look for harmonics
	Freq2 = list(Freq)
	harmo = dict()
	for f in Freq :
		f0 = f[0]
		harmo[f0] = list()
		Freq2.remove(f)
		for ff in Freq2 :
			tmp = f0/ff[0]
			if abs(tmp-ceil(tmp)) <= 0.01 :
				harmo[f0].append(ff)
	harmo2 = dict(harmo)
	for h in harmo2 :
		if len(harmo2[h]) == 0 :
			del harmo[h]
	
	# Then, we look for fundamentals (we will prefer frequencies with a higher magnitude as two 'sol' could otherwise be considered as harmonics)
	Fund = list()
	for h in harmo :
		tmp = harmo[h][0][1]
		for f in harmo[h] : # Frequencies are stored by increasing value
			if f[1] > tmp :
				Fund.append(f) # And a fundamental would be signaled by a sudden increased value of the frequency's magnitude
			tmp = f[1]

	# Then, we look for the notes that have been played
	# In general, each note is identified by a frequency, a name and a position on the keyboard (numbered from the left to the right, from 1 to 88 in general) and the correspondance is stored in table_ref. Notes will only be a list of the position of the note and its intensity.

	Notes = list()
	for f in Fund :
		for note in table_ref :
			if abs(f[0]/table_ref[note][0]-1) < 0.012 :
				Notes.append([note,f[1]]) # Position (1-88 from left to right) and intensity (0-255 from minimum to maximum)

	return Notes


