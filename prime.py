# -*- coding: utf-8 -*-

from math import ceil


def prime_test(number) :

	prime = True
	k = 2 

	while k < ceil(number/2)+1 :
		if number%k == 0 :
			prime = False
		k+=1

	return prime


def decomp(number) :

	coord = list()

	if prime_test(number) :
		coord.append(number)
	else :
		k = 2

		while k < number-1 :
			if number%k == 0 :
				if prime_test(k) :
					coord.append(k)
				else :
					coord = coord + decomp(k)

			k+=1

	return coord


def clean(l) :
	m = list()
	i = 0
	for elt in l :
		j = 0
		double = False
		for el in l[i+1:] :
			if el == elt :
					double = True	
			j+=1
		if not double :
			m.append(elt)
		i+=1

	return m



def exp(l,number) :
	exp = list()

	for elt in l :
		k = 1
		while number%(elt**k) == 0 :
			k+=1
		exp.append(k-1)

	return exp



def verify(l,m) :
	i = 0
	result = 1
	for elt in l :
		result *= l[i]**m[i]
		i+=1
	return result


number = int(input("Enter a natural integer\n"))

#number = 12479954200863

l = decomp(number)

l = clean(l)

m = exp(l,number)

r = verify(l,m)

print(l,m,r)

"""

m = list()

i = 2
while i <= number :
	tmp = decomp(i)
	if tmp == i :
		m.append(i)
	else :
		m = m + tmp
	i+=1

m = clean(m)
print(m, len(m))
"""
