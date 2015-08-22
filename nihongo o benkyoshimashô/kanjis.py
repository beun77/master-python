# -*- coding : utf-8 -*-

from PIL import Image
from random import randrange
from math import ceil
import sys
import psutil


# We ask the player what mode he wants to play

mode = 0
romajis_file = open("romajis.txt",'r')
menu_flag = 1


while (menu_flag == 1) :


	while (mode != 1 and mode != 2 and mode != 3 and mode != 4 and mode != 5) :
		print("\n\n\n\n##############################\n" + "##                          ##\n"  + "##  kanji o benkyôshimashô  ##\n" +"##                          ##\n" + "##############################\n") 
		print("Choose a game mode\n\n1. From kanjis to romajis\n2. From romajis to kanjis\n3. Reading mode\n4. Writing mode\n\n5. Exit\n")
		mode = int(input())



	# Exit

	if (mode == 5) :
		menu_flag = 0
		romajis_file.close()
		sys.exit()

	rounds = 0

	while (rounds <= 0) :
		print("How many rounds do you want to play ?")
		rounds = int(input())


	score = 0
	rounds_copy = rounds
	romajis_list = str(romajis_file.read()).split(" ")


	while (rounds > 0) :


		# Then we choose a kanji and its romaji transcription for him


		i = randrange(len(romajis_list))

		
		romajis = romajis_list[i]

		flag = 0
		for elt in romajis :
			if (elt == "-") :
				flag = 1

		if (flag == 1) :
			romajis = romajis.split("-")
		
		I = i + 1	
		kanji = Image.open("%s.jpg"%I)

		answer = str()



		# The player can now play

		# 1st mode

		if (mode == 1) :
			print("Enter one of the possible readings of the following kanji\n")
			kanji.show(command = "eog")
			answer = str(input())
			
			k = 0
			
			if (flag == 1) :
				for elt in romajis :

					if (elt == answer) :
						k += 1
			else :
				if (romajis == answer) :
					k += 1

			if k != 0  :
				score += 1
				print("\nRight\n\n")
			else :
				print("\nWrong\n\n")
			kanji.close()




		# 2nd mode
		
		if (mode == 2) :

			j = i
			k = i

			
			while (j == i) :
				j = randrange(len(romajis_list))
			while (k == i) :
				k = randrange(len(romajis_list))

			J = j + 1
			K = k + 1
			kanji_j = Image.open("%s.jpg"%J)
			kanji_k = Image.open("%s.jpg"%K)

			if (flag == 1) :
				print("Enter the number of the kanji corresponding to the following readings\n" + ", ".join(romajis) + "\n")
			else :
				print("Enter the number of the kanji corresponding to the following reading\n" + romajis + "\n")

			if (i <= j) :
				if (j <= k) :
					kanji.show(command = "eog")
					kanji_j.show(command = "eog")
					kanji_k.show(command = "eog")
				elif (k >= i) :
					kanji.show(command = "eog")
					kanji_k.show(command = "eog")
					kanji_j.show(command = "eog")
				elif (k <= i) :
					kanji_k.show(command = "eog")
					kanji.show(command = "eog")
					kanji_j.show(command = "eog")
			else :
				if (j >= k) :
					kanji_k.show(command = "eog")
					kanji_j.show(command = "eog")
					kanji.show(command = "eog")
				elif( i <= k) :
					kanji_j.show(command = "eog")
					kanji.show(command = "eog")
					kanji_k.show(command = "eog")
				elif( i >= k ) :
					kanji_j.show(command = "eog")
					kanji_k.show(command = "eog")
					kanji.show(command = "eog")


			answer = int(input())

			if answer == I :
				score += 1
				print("\nRight\n")
			else :
				print("\nWrong\n")

		

		# 3rd mode

		if (mode == 3) :
			meaning_file = open("meaning.txt",'r')
			meaning_list = str(meaning_file.read()).split(" ")
			meaning = meaning_list[i]
			

			flag = 0
			flag2 = 0

			for elt in meaning :
				if (elt == "-") :
					flag = 1
				if (elt == "_") :
					flag2 = 1
			if (flag == 1) :
				meaning = meaning.split("-")
				for elt in meaning :
					if (flag2 == 1) :
						elt = " ".join(elt.split("_"))
			else :
				if (flag2 == 1) :
					meaning = " ".join(meaning.split("_"))

			kanji.show(command = "eog")

			print("Enter one of the possible meaning of the following kanji\n")
			answer = str(input())

			correct_flag = 0

			if (flag == 1) :
				for elt in meaning :
					if (elt == answer) :
						correct_flag += 1
				
			else :
				if (answer == meaning) :
					correct_flag += 1

			if (correct_flag == 0) :
				print("\nWrong\n\n")
			else :
				score += 1
				print("\nRight\n\n")




		# 4th mode

		if (mode == 4) :
			meaning_file = open("meaning.txt",'r')
			meaning_list = str(meaning_file.read()).split(" ")
			meaning = meaning_list[i]
			

			flag = 0
			flag2 = 0

			for elt in meaning :
				if (elt == "-") :
					flag = 1
				if (elt == "_") :
					flag2 = 1
			if (flag == 1) :
				meaning = meaning.split("-")
				for elt in meaning :
					if (flag2 == 1) :
						elt = " ".join(elt.split("_"))
			else :
				if (flag2 == 1) :
					meaning = " ".join(meaning.Split("_"))


			j = i
			k = i

			
			while (j == i) :
				j = randrange(len(romajis_list))
			while (k == i) :
				k = randrange(len(romajis_list))

			J = j + 1
			K = k + 1
			kanji_j = Image.open("%s.jpg"%J)
			kanji_k = Image.open("%s.jpg"%K)


			if (i <= j) :
				if (j <= k) :
					kanji.show(command = "eog")
					kanji_j.show(command = "eog")
					kanji_k.show(command = "eog")
				elif (k >= i) :
					kanji.show(command = "eog")
					kanji_k.show(command = "eog")
					kanji_j.show(command = "eog")
				elif (k <= i) :
					kanji_k.show(command = "eog")
					kanji.show(command = "eog")
					kanji_j.show(command = "eog")
			else :
				if (j >= k) :
					kanji_k.show(command = "eog")
					kanji_j.show(command = "eog")
					kanji.show(command = "eog")
				elif( i <= k) :
					kanji_j.show(command = "eog")
					kanji.show(command = "eog")
					kanji_k.show(command = "eog")
				elif( i >= k ) :
					kanji_j.show(command = "eog")
					kanji_k.show(command = "eog")
					kanji.show(command = "eog")

			if (flag == 1) :
				print("Enter the number of the kanji corresponding to the following meanings\n" + ", ".join(meaning))

			else :
				print("Enter the number of the kanji corresponding to the following meaning\n" + meaning + "\n")

			answer = int(input())

			

			if (answer != I):
				print("\nWrong\n\n")
			else :
				score += 1
				print("\nRight\n\n")


			

		for proc in psutil.process_iter() :
			if (proc.name() == "display") :
				proc.kill()


		rounds -= 1		


	# The game is over

	score = ceil(score*1000/rounds_copy)/10

	if score < 20 :
		print("VERY POOR\n")
	elif score < 40 :
		print("POOR\n")
	elif score < 60 :
		print("AVERAGE\n")
	elif score < 80 :
		print("GOOD\n")
	else :
		print("EXCELLENT\n")

	print("Score : %d\n"%score)

	mode = 0
	menu_flag = 1




