		#############################
		##                         ##
		##    C O N V E R T E R    ##
		##           v2.0          ##
		##                         ##
		#############################

		    by Benoit Porteboeuf


	HOW TO USE THIS SOFTWARE ?

1. Select all pictures in the folder and copy them into the file "list.txt".
2. Open a terminal and go to this directory.
3. Type "python convert.py".
4. Enter your final format. Available formats currently are jpg, bmp, png, tiff, gif.
5. Enjoy !


	WHAT LAUNCHING OPTIONS ARE AVAILABLE ?

You can set launching options by typing "python convert.py -XXXX" in your terminal.
Those options are :

-h : Displays the help menu
-f : Activates a faster algorithm without damaging the image quality
-r : Replace your original pictures by the converted ones
-z : Compress all your converted pictures into a zip file
-R : Activates the recursivity search for pictures in your current folder