# -*- coding: utf-8 -*-


from PIL import Image
from math import ceil


picture = Image.open("test.png")
RGB_list = picture.split()
R = RGB_list[0]
G = RGB_list[1]
B = RGB_list[2]
size = picture.size

R_list = R.getdata()
G_list = G.getdata()
B_list = B.getdata()

Min_R = 255
Max_R = 0

for elt in R_list :
	if elt > Max_R :
		Max_R = elt
	if elt < Min_R :
		Min_R = elt

Min_G = 255
Max_G = 0

for elt in G_list :
	if elt > Max_G :
		Max_G = elt
	if elt < Min_G :
		Min_G = elt

Min_B = 255
Max_B = 0

for elt in B_list :
	if elt > Max_B :
		Max_B = elt
	if elt < Min_B :
		Min_B = elt
	
for elt in R_list :
	elt = ceil(elt*(255/Min_R - 255/(1/Max_R - 1/Min_R)) + 255/(1 - Max_R/Min_R))

for elt in G_list :
	elt = ceil(elt*(255/Min_G - 255/(1/Max_G - 1/Min_G)) + 255/(1 - Max_G/Min_G))

for elt in B_list :
	elt = ceil(elt*(255/Min_B - 255/(1/Max_B - 1/Min_B)) + 255/(1 - Max_B/Min_B))



picture.close()



