# -*- coding: utf-8 -*-

import math

num = int(input("Enter a natural integer for conversion\n"))



def decimal_to_binary(num_dec) : 	#bigindian
	tmp = num
	num_bin = list()
	k = ceil(log(num)/log(2)) + 1
	while k >= 1 :
		if num % (2**k) == 0 :
			num_bin = [1] + num_bin
			tmp = num/k
		else
			num_bin = [0] + num_bin
		k-=1
	return num_bin


def binary_to_decimal(num_bin) :
	num_dec = 0
	k = 0
	for elt in num_bin :
		num_dec = num_dec + elt*(2**k)
		k+=1
	return num_dec


def binary_to_complex(num_bin) :
	n = num[:2]
	s = num[3]
	o = num[4:]
	num_comp = 0



	a = (n-A)*cos(o-B)
	b = (n-A)*sin(o_B)

	return num_comp
	


def complex_to_binary(num_comp) :	
	num_bin = 0


	return numbin
