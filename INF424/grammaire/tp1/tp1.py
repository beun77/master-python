# -*- coding : utf-8 -*-


import re



def intro() :
	r = re.compile(r"[a-rt-z]*s[a-z]*")
	# ou r = re.compile(r"[a-z]*s[a-z]*")

	exp = "Le bon chasseur sachant chasser sait chasser sans son chien"

	m = r.findall(exp) # Trouve tous les mots contenant un 's' et renvoie une liste
	print(m)

	for elt in r.finditer(exp) : # Trouve tous les mots contenant un 's' et renvoie des match object itérables
		print(elt.group())


	r = re.compile(r"s+([a-z]+)") # ([a-z]+) -> crée un groupe \1
	m = r.sub(r"ch\1",exp) # Chaîne de remplacement \1 pour la fin du mot ? -> Permet de ne pas remplacer les 's' en fin de mots
	print(m)


	def ecrire_en_hexa(entree) :
		return hex(int(entree.group()))

	r = re.compile(r"[0-9]+")
	m = r.sub(ecrire_en_hexa,"toto 123 blabla 456 titi") # Applique la fonction de conversion sur les objets ayant matché la recherche
	print(m)

	return

#intro()



def Exercice1() : # Renvoie les informations relatives à PAUL
	r = re.compile(r"^([0-9]+);[^;]*;PAUL;") # Cherche des chiffres, puis un ';', puis tout ce qui n'est pas un ';', puis un ';', 'puis PAUL', puis un ';'
	f = open("gen1551.csv",'r')
	for ligne in f :
		for m in r.finditer(ligne) :
			print(m.group(1) + " OK")
	f.close()

	return

#Exercice1()

def Exercice2() : # Renvoie les informations relatives aux habitantes d'un village commençant par 'PLOU'
	r = re.compile(r"^([0-9]+);[^;]*;PLOU;")
	f = open("gen1551.csv",'r')
	l = 1
	for ligne in f :
		print(l,ligne)
		for m in r.finditer(ligne) :
			print(m.group(1) + " OK")
		l+=1
	f.close()

	return

#Exercice2()


def Exercice3() : # Remplace 'PLOU' par 'LOC' au début des noms de villages
	r = re.compile(r"^(([0-9]+);[^;]*;)PLOU;")
	f = open("gen1551.csv",'r')
	l = 1
	s = str()
	for ligne in f :
		print(l,ligne)
		ligne = r.sub(r'\1LOC',ligne)
		l+=1
		s = s + ligne + "\n"
	f.write(s)
	f.close()
	return

#Exercice3()



def Exercice4() : # Incrémente les dates de naissances de tous les 'PAUL' habitant à 'PLOU*'  de 10 ans
	r = re.compile(r"^(([0-9]+);[^;]*;)PAUL;") # Cf corrigé sur Moodle (groupe 1, dates, groupe 2)
	f = open("gen1551.csv",'r')
	l = 1
	s = str()
	for ligne in f :
		print(l,ligne)
		ligne = r.sub(r'\1LOC',ligne)
		l+=1
		s = s + ligne + "\n"
	f.write(s)
	f.close()
	return

#Exercice4()


def Exercice5() : # Compte le nombre de fiches de personnes nommées 'ABALAIN'
	r = re.compile(r"^[0-9]+;ABALAIN;")
	f = open("gen1551.csv",'r')
	l = 0
	for ligne in f :
		if r.match(ligne) :
			l+=1
	f.close()
	print(l)
	return

#Exercice5()

# Exercice6 -> Cf Moodle
