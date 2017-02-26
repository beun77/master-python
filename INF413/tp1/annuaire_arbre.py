# -*- coding : utf-8 -*-



####################
# NOEUD
####################



class noeud :

	def __init__(self, name, number) : #Initializes the node
		self.name = name
		self.number = number
		self.right = None
		self.left = None
		self.parent = None
		return
		
	def __str__(self) : #Prints the content of the node
		if self is None :
			return print("None")
		else :
			return print(self.name + " : " + self.number)

	def __eq__(self, name, number) : #Returns if the node is equal to a given one (boolean)
		if len(self.name) != 0 and len(self.number) != 0 :
			return (self.name == name and self.number == number)
		else :
			return None

	def __sup__(self, node) : # Returns if the current node is superior or not to a given node (boolean)
		current = self.__toint__()
		new = node.__toint__()
		if len(current) < len(new) :
			l = len(current)
		else :
			l = len(new)
		for i in range(0, l) :
			if current[i] < new[i] :
				return False
			elif current[i] > new[i] :
				return True
		return len(current) > len(new)

	def __inf__(self, node) : # Returns if the current node is inferior or not to a given node (boolean)
		current = self.__toint__()
		new = node.__toint__()
		if len(current) < len(new) :
			l = len(current)
		else :
			l = len(new)
		for i in range(0, l) :
			if current[i] > new[i] :
				return False
			elif current[i] < new[i] :
				return True
		return len(new) > len(current)


	def __toint__(self) :
		name = self.name
		alpha = 'abcdefghijklmnopqrstuvwxyz'
		score = list()
		for elt in name.lower() :
			i = 0
			for el in alpha :
				if el == elt :
					score.append(i)
					break
				i += 1
		return score


####################
# DICTIONNAIRE
####################


class dictionnaire :

	def __init__(self) : #Initializes the dictionary 
		self.root = None
		self.length = 0
		return

	def append(self, node) : #Adds a node in the binary research tree
		ro = self.root
		if ro is None :
			self.root = node
			self.length += 1
		else :
			Next = True 
			r = ro.right
			l = ro.left
			nd = ro
			nd2 = nd	
			while Next == True :
				if node.__sup__(nd) :
					nd = nd.right
				elif node.__inf__(nd) :
					nd = nd.left
				else :
					print("This node "+node.name+" is already in the tree")
					return
				if nd is None :
					break
				nd2 = nd
			if node.__sup__(nd2) :
				nd2.right = node
				node.parent = nd2
				self.length += 1
			else :
				nd2.left = node
				node.parent = nd2
				self.length += 1
			return

	def delete(self, node) : #Deletes a given node from the tree
		if self.search(node)[1] :
			if node.left is None and node.right is None :
				parent = node.parent
				node.parent = None
				if parent.left == node :
					parent.left = None
				else :
					parent.right = None
			elif node.left is None :
				parent = node.parent
				child = node.right
				child.parent = parent
				if parent.left == node :
					parent.left = child
				else :
					parent.right = child
			elif node.right is None :
				parent = node.parent
				child = node.left
				child.parent = parent
				if parent.left == node :
					parent.left = child
				else :
					parent.right = child
			else :
				#On supprime son successeur	ou prédécesseur immédiat qui a au plus un fils, on supprime le noeud voulu qui n'a donc plus qu'un fils et on rajoute le successeur ou prédécesseur immédiat précédemment supprimé
				#Successeur immédiat : supérieur au noeud, inférieur à tous les autres -> fils droit
				self.delete(node.right)
				self.delete(node)
				self.append(node.right)
			return
		else :
			return



	def search(self, node) : # Searches for a node in the tree
		nd = self.root
		nd2 = nd
		Next = True
		while Next == True :
			if node.__sup__(nd) :
				nd = nd.right
			elif node.__inf__(nd) :
				nd = nd.left
			else :
				return print("1 entry found : "+node.name+", "+node.number), True

		return print("No entry found for : "+node.name), False

	


	def leng(self) : #Returns the length of the tree
		return self.length

	"""
	def explore(self, start) : #Explores the tree via a recursive method
		start2 = list(start)
		for node in start :
			start2.remove(node)
			if node.right is not None :
				start2 + self.explore(node.right)
			if node.left is not None :
				start2 + self.explore(node.left)
			if node.left is None and node.right is None :
				return start2
		return start2
	
	def disp(self) : #Displays the list
		nd = self.root
		string = str()
		for elt in self.explore(self.root) :
			string += elt.name + " : " + elt.number
		return print(string)
	"""

	def ld(self, File) : #Loads a file into a list
		fl = open(File, 'r')
		f = fl.read()
		f = f.split("\n")
		i = 0
		for elt in f :
			if len(elt) != 0 :
				g = elt.split(",")
				nd = noeud(g[0],g[1])
				self.append(nd)
				i+=1
		return


####################
# MAIN
####################



print("Starting main programm")
Ann = dictionnaire()
print("Opening file")
Ann.ld("noms_100.csv")
print("File opened")
print("Number of entries: "+str(Ann.leng()))
n = noeud('Benoit', '305723113')
Ann.search(n)
n = noeud('Benoit', '305723113')
Ann.delete(n)


print("Done")

