# -*- coding : utf-8 -*-

##///////////////////////////////////##
##   T H E   L I G H T   P I A N O   ##
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##

import generate_sin
import subprocess as sp
import numpy
from math import ceil
#import soundfile as sf

compatible = ['s16p','s8p','16p','8p','s16','s8','16','8'] # Compatible types of encoding

def get_infos(path) : # Reads infos about a mp3 file

	error = str()
	FFMPEG_BIN = "ffmpeg" # Source of the following code: http://zulko.github.io/blog/2013/10/04/read-and-write-audio-files-in-python-using-ffmpeg/

	pipe = sp.Popen([FFMPEG_BIN,"-i", path, "-"],stdin=sp.PIPE, stdout=sp.PIPE,  stderr=sp.PIPE) # This gets the file's informations
	pipe.stdout.readline()
	pipe.terminate()
	infos = pipe.stderr.read()
	infos = str(infos).split(' ')
	Duration = '00:00:01'
	fsampling = 44100
	#print('INFORMATIONS',infos)
	for i in range(0,len(infos)) : # But we are only interested in its duration and its sampling frequency
		if str(infos[i]) == 'Duration:' :
			Duration = str(infos[i+1])
		if str(infos[i]) == 'Audio:' :
			fsampling = int(infos[i+2]) # in Hz
			nb_channels = infos[i+4]
			encoding = infos[i+5]

	if nb_channels == 'stereo,' :
		nb_channels = 2
	elif nb_channels == 'mono,' :
		nb_channels = 1
	else :
		error = 'channels'
		return 1,1,'','',1,error
	
	Duration = Duration[:len(Duration)-2]
	Duration = Duration.split(':')
	d = 0
	for elt in Duration :
		d = 60*d + ceil(float(elt)) # in seconds
	#print('DURATION',d,'FSAMPLING',fsampling)
	form = str()

	encoding = encoding[:len(encoding)-2]
	if encoding not in compatible :
		error = 'encoding'
		return 1,1,'','',1,error

		if encoding[0] == 's' : # Signed numbers
			form += 'int'
		if encoding[1] == '1' :
			form += '16' # 16 bits samples
		else :
			form += '8'
	else :
		form += 'uint'
		if encoding[0] == '1' :
			form += '16'
		else :
			form += '8'
	if encoding[len(encoding)-1] == 'p' : # Type of buffer organization for multi channels files
		buff = 'p' # planar
	else :
		buff = 'not_p'
	# -> In infos, there's stereo or mono + the type of encodage (ex: s16p) which explains the nature of the numbers (signed or unsigned), their size (8 or 16 bits) as well as their organization in the buffer (c1c1c2c2c1c1c2c2 or c1c1c1c1c2c2c2c2). For more informations: http://stackoverflow.com/questions/18888986/what-is-the-difference-between-av-sample-fmt-s16p-and-av-sample-fmt-s16

	return d,fsampling,form,buff,nb_channels,error




def read_music(path) : # Reads a mp3 file at the given path and returns the list of samples as well as the sampling frequency.
	

	# Method 1 - Using FFMPEG

	FFMPEG_BIN = 'ffmpeg'

	d,fsampling,form,buff,nb_channels,error = get_infos(path)
	if error == 'channels' :
		print('This format is not compatible with our software. Please try a mono or stereo recording.')
		return [],1,False
	elif error == 'encoding' :
		print('This format is not compatible with our software. Please try one of the following encoding: '+compatible)
		return [],1,False

	else :

		command = [FFMPEG_BIN,'-i', path,'-f', 's16le','-acodec', 'pcm_s16le','-ar', str(fsampling),'-ac', '1','-'] # The file is always read as a mono recording
		pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10**8)
		#raw_audio = pipe.proc.stdout.read(88200*4) #88200 frames of 4 bits integer ie two seconds of music
		raw_audio = pipe.stdout.read(d*fsampling*4) # This should read the whole file
		audio_array = numpy.fromstring(raw_audio, dtype = form) # And this should transform the binary sequence in an array of integers

		"""
		f = open('audio_data.txt','w')
		for elt in audio_array :
			f.write(str(elt)+'\n')
		f.close()	
		"""

		Samples = list()

		#print('NB SAMPLES',len(audio_array),'NB_CHANNELS',nb_channels,'SAMPLING FREQUENCY',fsampling,'DURATION',d)
		"""
		if nb_channels == 1 : # mono
			if form[0] == 'u' : # unsigned
				for elt in audio_array :
					Samples.append(elt)
			else :
				for elt in audio_array :
					Samples.append(abs(elt)) # /!\ signed
		else : # stereo
			if form[0] != 'u' : # /!\ signed
				audio_array = abs(audio_array)
			if buff == 'p' : # planar
				#for i in range(0,ceil(len(audio_array)/2)) :
				#	numpy.append(Samples,[ceil((audio_array[i]+audio_array[2*i])/2)]) # /!\ Run Time Error
				for i in range(0,ceil(len(audio_array)/2)-1) :
					Samples.append(ceil((audio_array[2*i]+audio_array[2*i+1])/2))
			else : # unplanar
				#for i in range(0,len(audio_array)-2) :
					numpy.append(Samples,[ceil((audio_array[i]+audio_array[i+2])/2)]) # /!\ Run Time Error
				#
				for i in range(0,ceil(len(audio_array)/2)-1) :
					Samples.append(ceil((audio_array[2*i]+audio_array[2*i+1])/2))
		"""
		for elt in audio_array :
			Samples.append(elt)


		# This conversion might be useless as ffmpeg seems to already convert stereo s16p to mono s16

		#print('raw_audio',raw_audio,'audio_array',audio_array) # 2 remaining informations to get: 1) size of encoding (8 or 16 bits), 2) signed or unsigned number + (if big or little endian, use struct.unpack(something))


		return Samples, fsampling,True

		"""
		# Method 2 - Converting to .wav then reading with PySoundFile

		#command = ['ffmpeg', '-i', path, '-vn', '-acodec', 'pcm_s16le', '-ac', '1', '-ar', '44100', '-f', 'wav', path[:len(path)-3]+'wav']
		music =  path[:len(path)-3]+'wav'
		command  = ['mpg123', '-w',music,path]
		pipe = sp.Popen(command)
		#print('MUSIC',music)
		Signal,fsampling = sf.read(music)
		print('SIGNAL',Signal) # Signal seems empty, but it has a shape - the shape describes it as 0 frames and 2 channels
		shape = Signal.shape
		number_channels = shape[1]

		if number_channels == 2 :
			print('STEREO SOUND DETECTED') # We only want mono

		Samples = [0,0]
		return Samples,fsampling
		"""

def read_tlp(path) : # Reads the .tlp files to produce the light animation
	print("Unavailable function at the moment")
	f = open(path,'r')
	flist = f.read().split('\n')

	fsampling = flist[0][1:]
	del flist[0]
	del flist[1]
	del flist[len(flist)-1]

	flist = (''.join(flist)).split('s') # We split the file accoring to its frames/samples

	Notes = list()
	tmp = list()

	for sample in flist :
		for note in elt.split('p') :
			tmp.append(note.split('m'))
		Notes.append(tmp)

	f.close()
	return fsampling,Notes # A list of samples = A list of list of notes = A list of list of a position and a magnitude




def read_test() : # Returns the list of generated samples as well as the sampling frequency.

	print("Using generated signals...")

	N = 1000
	W1 = 40
	W2 = 15000
	k = 100
	f = 40000

	A = generate_sin.generate_signal(N,W1,W2,k,f)

	return A,f


