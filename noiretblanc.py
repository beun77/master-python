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

BW_list = list()

i = 0

for elt in R_list :
	BW_list.append(ceil((elt + G_list[i] + B_list[i])/3))
	i+=1


infos_picture = open("infos_picture.txt","w")
infos_picture.write(" ".join(str(BW_list)))


picture.close()
infos_picture.close()



