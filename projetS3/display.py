# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##

import time
import RPi.GPIO as GPIO
from math import ceil


def convert(magnitude,magnitude_max,threshold) : # Converts the entry magnitude from 0 to magnitude_max to a magnitude from 1 to thresold+1

	magnitude = ceil(magnitude*threshold/magnitude_max)+1

	return magnitude


def disp(Notes,fsampling,frefresh,ref_table) : #Displays the notes to play on the LED matrix

	print("Unavailable function at the moment")

	# First, we need to create all the threads for the matrix display

	threads = dict()

	for sample in Notes :
		threads[sample] = list()
		for note in ref_table :
			for n in Notes[sample] :
				if note == n[0] : # The note is played
					threads[sample].append(convert(n[1]),255,3)
				else : # The note is not played
					threads[sample].append(0)

	# Then, we need some clocks to trigger the shift registers

	# Then, we need to address the whole LED matrix

	for sample in threads :
		light(threads[sample:sample+3],fsampling,frefresh)

	return



def screen_disp(something) : # Displays something on a black and white small LCD display

	print("Unavailable function at the moment")

	return



def greetings() : #Displays a greeting signal when turning on the device (+ the console)

	log = open('logo.tlp','r') # Console signal
	logo = log.read()
	logo = logo.split('<new>')[0]
	print(logo)
	log.close()

	screen_disp('THE LIGHT PIANO')

	disp('Welcome') # LED Signal - Pause
	
	screen_disp('WELCOME')

	return


def see_you() : #Displays a good bye signal when turning the device off (+ the console)

	log = open('logo.tlp','r') # Console signal
	logo = log.read()
	logo = logo.split('<new>')[1]
	print(logo)
	log.close()

	screen_disp('SEE YOU SOON')

	disp('SeeYouSoon') # LED signal - Pause

	screen_disp('THE LIGHT PIANO')

	return



