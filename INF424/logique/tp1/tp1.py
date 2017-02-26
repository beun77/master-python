# -*- coding: utf-8 -*-

		#############################
		## INF 424 - LOGIQUE - TP1 ##
		#############################


import nltk


for elt in ["la fille porte une robe rouge","la fille dort","la fille dort une robe rouge","la fille porte","la fille parle à un ami","la fille parle un ami","la fille porte à une robe rouge","les filles parlent à un ami","les filles portent des robes rouges","les filles parle à une amie","les filles parlent à une ami","la fille portent un robes rouge"] :

	sent = elt.split()
	parser = nltk.load_parser("file:grammaire.fcfg")

	Correct = False

	for tree in parser.parse(sent):
		print(tree)
		tree.draw()
		Correct = True

	if not Correct :
		print("Cette phrase \'"+elt+"\'  est grammaticalement incorrecte")


