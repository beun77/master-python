from random import randrange as randrange


class Aef:
    pass

class Aef1(Aef):
    def accepte(self, text):
        etat = 1

        for char in text:
            # Traitement des characteres de la chaine
            if etat == 1 and char == "a":
                etat = 2
            elif etat ==2 and char == "b":
                etat = 1
            else:
                # Il n'y a pas de transition correspondante
                return False

        # il n'y a plus rien a lire. Est-on dans un etat terminal?
        if etat == 2:
            return True
        else:
            return False




class Aef2(Aef): # Version naïve de l'aef 2
	def accepte(self, text):
		etat = 0

		for char in text:
			# Traitement des characteres de la chaine
			if etat == 0 and char == "a":
				etat = 1
			elif etat == 1 and char == "b":
				etat = 2
			elif etat == 2 and (char == "a" or char == "b"):
				etat = 3
			elif etat == 3 and char == "b":
				etat = 4
			elif etat == 3 and char == "a":
				etat = 3
			elif etat == 4 and char == "a":
				etat = 5
			elif etat == 4 and char == "b":
				etat = 4
			elif etat == 5 and char == "b":
				etat = 4
			elif etat == 5 and char == "a":
				etat = 3
			else:
				# Il n'y a pas de transition correspondante
				return False

        # il n'y a plus rien a lire. Est-on dans un etat terminal?
		if etat == 2:
			return True
		else:
			return False




class Aef22(Aef): # Version plus optimisée de l'aef 2

	table = dict()
	Init = list()
	Final = list()

	def __init__(self) :
		"""
		null_list = list()

		for i in range(0,6) :
			null_list += ["NULL"]

		for i in range(0,6) :
			self.table[i] = null_list #Notre matrice est initialisée. Remplissons la à l'aide des relations
		"""

		T = dict(self.table)
		n = "NULL"
		T[0] = [n,'a',n,n,n,n]   #La clé primaire correspond à l'état courant, la liste correspond aux conditions nécessaires pour passer à l'état suivant
		T[1] = [n,n,'b',n,n,n]
		T[2] = [n,n,n,'ab',n,n]
		T[3] = [n,n,n,'a','b',n]
		T[4] = [n,n,n,n,'b','a']
		T[5] = [n,n,n,'a','b',n]

		self.Init = [0]
		self.Final = [2,5]

		self.table = dict(T)

		return



	def accepte(self, text,e):
		if e <= len(self.Init) :
			etat = self.Init[e] #On commence par l'état initial e
		else :
			etat = self.Init[0]


		for char in text:
			# Traitement des characteres de la chaine
			pos = 0
			suivant = False
			for cond in self.table[etat] :
				if suivant == False : #Si pas d'état suivant trouvé, on continue de parcourir les transitions possibles dans l'état courant
					if cond != "NULL" :
						for lett in cond : #Une transition peut avoir plusieurs conditions (a ou b)
							if lett == char : #Condition vérifiée
								etat = pos #Changement d'état
								suivant = True
					pos += 1
				else: #Si on a trouvé un état suivant, on s'arrête là
					break

        # il n'y a plus rien a lire. Est-on dans un etat terminal?
		accepted = False
		for final in self.Final :
			if etat == final :
				accepted = True
		return accepted


class Aef3(Aef): # Version de l'aef 3

	table = dict()
	Init = list()
	Final = list()

	def __init__(self,T,Init,Final) :
		self.Init = Init
		self.Final = Final
		self.table = dict(T)
		return

	def accepte(self, text,e):
		if e <= len(self.Init) :
			etat = self.Init[e] #On commence par l'état initial e
		else :
			etat = self.Init[0]

		for char in text:
			# Traitement des characteres de la chaine
			suivant = False
			#alea = randrange(0,6) # Il faut générer un tableau d'entiers compris entre 0 et 5 et ordonnées de manière aléatoire
			alea = [2,4,3,0,1,5]
			condi = list()
			for f in alea :
				condi += [{self.table[etat][f],f}]
			for cond in condi : #Attention, il faut pouvoir simuler un automate non déterministe. L'aléatoire est donc de mise.
				if suivant == False : #Si pas d'état suivant trouvé, on continue de parcourir les transitions possibles dans l'état courant
					if cond[0] != "NULL" :
						for lett in cond[0] : #Une transition peut avoir plusieurs conditions (a ou b)
							if lett == char : #Condition vérifiée
								etat = cond[1] #Changement d'état
								suivant = True
				else: #Si on a trouvé un état suivant, on s'arrête là
					break
        # il n'y a plus rien a lire. Est-on dans un etat terminal?
		accepted = False
		for final in self.Final :
			if etat == final :
				accepted = True
		return accepted







if __name__ == "__main__":
    #aef = Aef1()
    #aef = Aef2()
    #aef = Aef22()

	T = dict()
	n = "NULL"
	T[0] = [n,'a',n,n,n,n]   #La clé primaire correspond à l'état courant, la liste correspond aux conditions nécessaires pour passer à l'état suivant
	T[1] = [n,n,'b',n,n,n]
	T[2] = [n,n,n,'ab',n,n]
	T[3] = [n,n,n,'ab','b',n]
	T[4] = [n,n,n,n,n,'a']
	T[5] = [n,n,n,n,n,n]
	Init = [0]
	Final = [2,5]

	aef = Aef3(T,Init,Final)
	while True:
		print("Veuillez entrer votre chaine de test")
		#text = raw_input()
		text = input()
		#if aef.accepte(text):
		if aef.accepte(text,0) :
			print("Chaine %s acceptee" % text)
		else:
			print("Chaine %s refusee" % text)




