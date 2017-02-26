# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##


from math import sin, ceil

def generate_signal(N,W1,W2,k,f) :	# Generates a list of N samples of a signal exclusively composed of pur sinus
	#N is the number of samplings, W1 and W2 the minimum and maximum frequency of the signal, k is the frequency step and f is the sampling frequency
	A = list()
	for n in range(0,N) : # N samples
		a = list()
		wmax = ceil(abs(W1-W2)/k+1)
		for w in range(0,wmax) : # Frequencies from W1 to W2 Hz
			a.append(100*sin((W1+w*k)*n/f))
		A += [ceil(abs(sum(a)))]
	#print(A)

	return A

#generate_signal(500,10,50,2,120)
