# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##

#import time
#import RPi.GPIO as GP


def disp(something) : #Displays the notes to play on the LED matrix

	print("Unavailable function at the moment")

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



