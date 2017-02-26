# -*- coding : utf-8 -*-


####################
# NOEUD
####################



class noeud :

	def __init__(self, name, number) : #Initializes the node
		self.name = name
		self.number = number
		self.next = None
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


####################
# LISTE
####################



class liste :

	def __init__(self) : #Initializes the list
		self.head = None 
		self.tail = None
		return

	def delete(self, n) : #Deletes a node in the list
		nd = self.head
		while 1 :
			nd2 = nd.next
			if nd2 is None :
				break
			elif nd2.__eq__(n.name,n.number) == True :
				nd3 = nd2.next
				nd.next = nd3
			nd = nd2
		return

	def insert(self, node) : #Inserts a node in the list (adds a node at the beginning of the list)
		node.next = self.head
		self.head = node
		return

	def append(self, node) : #Appends a node in the list (adds a node at the end of the list)
		nd = self.head
		if nd is None :
			self.insert(node)
		else :
			while 1 :
				nd2 = nd.next
				if nd2 is None :
					nd.next = node
					self.tail = node
					break
				else :
					nd = nd2
		return

	def search(self, n) : #Searches a node in the list
		nd = self.head
		t = self.tail
		while 1 :
			if nd.__eq__(n.name,n.number) == True :
				break
			elif nd.__eq__(t.name,t.number) == True :
				break
			else :
				nd = nd.next
		return nd.__str__()

	def leng(self) : #Returns the length of the list
		i = 0
		nd = self.head
		while nd :
			i+=1
			nd = nd.next
		return i

	def disp(self) : #Displays the list
		nd = self.head
		while nd :
			nd.__str__()
			nd = nd.next
		return

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
Ann = liste()
print("Opening file")
Ann.ld("noms_100.csv")
print("File opened")
print("Number of entries: "+str(Ann.leng()))
print(Ann.disp())
n = noeud('Benoit', '305723113')
print(Ann.search(n))
Ann.delete(n)
print(str(Ann.leng()))
print("No problem has been found.")
print("Done")

