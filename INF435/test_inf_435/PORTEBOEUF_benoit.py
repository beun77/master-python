# -*- Coding : utf-8 -*-

# Auteur : Benoit Porteboeuf
# Filière : FIG2A
# UV : MAJ INF 435

# AUTO-EVALUATION EN PYTHON

import sys, os


# EXERCICE 1

"""
print 'c'est celle-ci' # Ne peut marcher car il y a un nombre impair d'apostrophes
print "non c'est l'autre"; # Ne peut marcher à cause du point-virgule
print '''ou alors c'est cele-ci.''' # Peut marcher
print 'ou peut-être l'autre'. # Ne peut marcher car il y a un nombre impaire d'apostrophes et qu'il y a un point à la fin
"""



# EXERCICE 2

# Plusieurs possibilités s'offrent à nous. On se propose ici de réaliser simplement un dictionnaire de taille 5*n

#Notes = numpy.array([[' ', 1, 2, 3, 4], ['Dupont', 5, 16, 2, 7, 12], ['Durand', 3, 17, 5, 9, 11], ['Tartempion', 11, 18, 7, 10,13]])
print('Exercice 2\n\n')

Notes = {'Dupont':[5,16,2,7, 12], 'Durand':[3,17,5,9,11], 'Tartempion' : [3,17,5,9,11]}

# On peut alors obtenir la 4e note de Dupont selon :

note = Notes['Dupont'][3]

print(str(Notes) + "\n\n" + str(note) + "\n")




# EXERCICE 3

# Plusieurs possibilités s'offrent à nous. On se propose de faire une boucle for et une boucle while

print('Exercice 3\n\n')

#Wideness = Notes.shape[0]
#Height = Notes.shape[1]

Wideness = 4

for eleve in Notes :
	j = 0
	while j < Wideness :
		tmp = Notes[eleve][j] + 1
		if tmp <= 18 :
			Notes[eleve][j] = tmp
		j += 1

print(Notes)




# EXERCICE 4

print('Exercice 4\n\n')

# Plusieurs méthodes s'offrent à nous. On se propose ici de choisir une méthode un peu naïve mais particulièrement lisible


def harmoniser(Notes) :

	#Wideness = Notes.shape[0]
	#Height = Notes.shape[1]

	Wideness = 4
	Height = len(Notes)

	tmp = 0

	for eleve in Notes :
		j = 0
		while j < Wideness :
			tmp += Notes[eleve][j]
			j += 1

	moy = tmp/((Wideness)*(Height))

	print(moy)

	if moy < 10 :
		delta = 10-moy

		for eleve in Notes :
			j = 0
			while j < Wideness :
				Notes[eleve][j] += delta
				j += 1

	return Notes


Notes = {'Dupont':[5,16,2,7, 12], 'Durand':[3,17,5,9,11], 'Tartempion' : [3,17,5,9,11]}


print(harmoniser(Notes))




# EXERCICE 5

# Plusieurs méthodes sont là aussi possibles. On se propose de lire le fichier dans sa globalité et de le retrier sans faire appel aux raccourcis python tout en faisant attention aux éventuelles erreurs...

if len(sys.argv) > 1 :
	filename = str(sys.argv[1])
else :
	print("Error: no path entered")
	sys.exit(0)

folder = str(os.getcwd())

if os.path.exists(folder+'/'+filename) :
	original = open(folder+'/'+filename, 'r')
else :
	print("Error: Wrong path")
	sys.exit(0)

liste1 = original.read().split("\n")

liste2 = list()

for elt in liste1 :
	liste2 = [elt] + liste2

original.close()


print("\n".join(liste2))

