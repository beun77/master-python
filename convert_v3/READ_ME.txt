		#############################
		##                         ##
		##    C O N V E R T E R    ##
		##          v3.4.1         ##
		##                         ##
		#############################

		    by Benoit Porteboeuf
		porteboeuf.benoit@gmail.com


	DESCRIPTION

This software is designed to make converting pictures easier. It is a python program and uses the free library PIL to work.
Please note that you should have Python 2 or greater installed.


	HOW TO USE THIS SOFTWARE?

1. Select all pictures and copy them in the "original" folder. Compressed files can be read as well.
2. Open a terminal and go to the convert directory.
3. Type "python convert.py". You can use some launching options if you want or add the path to your pictures' folder.
4. Enter your final format. Available formats currently are jpg, png, bmp, gif, tiff, pdf.
5. All your converted files will be saved in the "computed" folder.


	WHAT LAUNCHING OPTIONS ARE AVAILABLE?

You can set launching options by typing "python convert.py -XXXX" in your terminal.
Those options are:

-f : Activates a faster algorithm without damaging the image quality
-h : Displays the help menu
-p : Adds a prefix of your choice to your pictures
-r : Replaces your original pictures by the converted ones
-R : Activates the recursivity search for pictures in your current folder
-s : Adds a suffix of your choice to your pictures
-S : Enables the resize option
-t : Compresses all your converted pictures into a .tar.gz file
-z : Compresses all your converted pictures into a .7z file


edited on 08.23.2015
