# -*- coding : utf-8 -*-


import math, random, sys


# Authors: Benoit PORTEBOEUF, Morgan ROBIN
# Date: 10.09.2015
# Course: MAJ INF-413



		########################################
		##                                    ##
		##  K-MEANS ALGORITHM IMPLEMENTATION  ##
		##                                    ##
		########################################



"""
This software implements a k-means algorithm. Data must be written in a file named 'data.txt' as follow: coord1, coord2, ..., coordn, string\ncoord1', ...
It will be possible to choose between different types of norm calculation - Euclidean and Manhattan are currently available.

There is two classes: point and group. A point is defined by its name (id), its coordinates and a string (for instance, its specie). A group is defined by a name (id), a center (point), and points.
"""



###################################
# CLASS DEFINITIONS
###################################


class point : # Name is the id (int) of the point, coordinate is a list of its coordinates and specie is a string that qualifies it
	def __init__(self,name,coordinates,specie) :
		self.name = name
		self.coordinates = coordinates
		self.specie = specie
		return

	def __str__(self) :
		return str(self.name) + str(self.coordinates) + str(self.specie)

	def __eq__(self, name) :
		if self.name == name :
			return True
		else :
			return False


class group : # A group is a set of points. Name is the id (int) of the group, center is the closest point to its isobarycenter and points is a list f its points.
	def __init__(self,name) :
		self.name = name
		self.center = None
		self.points = list()
		return

	def center(self, center) :
		self.center = center
		return
	
	def add(self,point) :
		self.points.append(point)
		return

	def remove(self,point) :
		self.points.remove(point)
		return

	def __str__(self) :
		s = str()
		for point in self.points :
			s += " "+str(point)
		return "group " + str(self.name) + " - " + "center: " + str(self.center) +" - points: " + s


######################################
# DISTANCE CALCULATION
######################################


def Distance(center,point,norm) : # Returns the distance between the center and the point according to the chosen norm
	if norm == "Euclidean" :
		return Euclidean(center, point)
	elif norm == "Manhattan" :
		return Manhattan(center, point)
	else : #norm == "Sup"
		return Sup(center, point)

def Euclidean(center, point): # Euclidean norm (norm 2)
	# center is a point type and is the reference, point is a point type
	tmp = 0
	l = len(center.coordinates)
	for i in range(0,l) :
		tmp+=(float(center.coordinates[i])-float(point.coordinates[i]))**2
	return math.sqrt(float(tmp))

def Manhattan(center, point) : # Manhattan norm (norm 1)
	tmp = 0
	l = len(center.coordinates)
	for i in range(0,l) :
		tmp += abs(float(center.coordinates[i])-float(point.coordinates[i]))
	return tmp

def Sup(center, point) : # Superior norm (norm infinite)
	tmp = 0
	l = len(center.coordinates)
	for i in range(0,l) :
		a = abs(float(center.coordinates[i])-float(point.coordinates[i]))
		if a >= tmp :
			tmp = a
	return tmp


#####################################
# INITIALIZATION
#####################################

def choose(k,data) : # Chooses k random centers in all the points
	centers = list()
	i = 0
	while i < k :
		tmp = random.randrange(len(data))
		if tmp not in centers :
			centers.append(tmp)
			i+=1
	return centers

def make_group(centers,data) : # Builds the initial groups with their centers only
	groups = dict()
	i = 0
	for elt in centers :
		Group = group(str(i))
		Group.center = data[elt]
		groups[i] = Group
		i+=1
	return groups

######################################
# LOOP INSTRUCTIONS
######################################

def optimizing(groups,data,norm) : # Calculates the distance of every point to every centers and optimizes groups
	for point in data : # Calculates the distances
		dist = list()
		for group in groups :
			dist.append(Distance(groups[group].center,data[point],norm))
		i = 0
		mini = dist[0]
		for elt in dist : # Finds the closest center and group
			if elt <= mini :
				mini = elt
				gr = i
			i+=1
		#print(dist,mini,gr,point)
		if point not in groups[gr].points : # Changes group if needed
			groups[gr].add(data[point])
			print("point "+str(point)+" added to group "+str(gr))
		for group in groups : # Removes the point from its previous group if needed
			if groups[group].name != groups[gr].name and data[point] in groups[group].points and groups[group].center != data[point] :
				groups[group].remove(data[point])
				print("point "+str(point)+" removed from group "+str(group))
	return groups

def new_centers(groups,centers,norm) : # Calculates the centers of the different groups
	centers2 = list()
	for group in groups : # Calculates the isobarycenter of every group
		bary = [0]
		gr = groups[group]
		for Point in gr.points :
			i = 0
			p = Point
			for coordinate in p.coordinates :
				if len(bary)-1 < i :
					bary.append(float(coordinate))
				else :
					bary[i] += float(coordinate)
				i+=1
		coordinates = list()
		for coordinate in bary :
			if len(gr.points)!=0 :
				coordinates.append(float(coordinate)/float(len(gr.points)))
		
		barycenter = point("bary"+str(group),coordinates," ")
		for Point in gr.points : # Finds the closest point to the calculated isobarycenter
			dist = list()
			dist.append(Distance(barycenter,Point,norm))
		dmin = dist[0]
		b = 0
		for i in range(len(dist)) :
			if dist[i] < dmin :
				dmin = dist[i]
				b = i
		centers2.append(gr.points[b].name) # Updates the center
		gr.center = gr.points[b]

	return groups,centers2


######################################
# TESTS
######################################


def verify_specie(groups) : # Verifies that every points in the same group have the same specie
	for group in groups :
		ref = groups[group].points[0].specie
		for point in groups[group].points :
			if point.specie != ref :
				return False
	return True

def verify_norms() : # Verifies that norms behave in a coherent way
	a = point('a',[0,1,2],' ')
	b = point('b',[1,0,2],' ')
	c = point('c',[2,1,0],' ')
	O = point('0',[0,0,0],' ')
	if Distance(a,a,'Euclidean') == 0 and Distance(a,a,'Sup') == 0 and Distance(a,a,'Manhattan') == 0 : # Separation
		if int(Distance(a,b,'Euclidean')**2) == 2 and int(Distance(a,b,'Sup')) == 1 and int(Distance(a,b,'Manhattan')) == 2 : # Result
			if Distance(a,O,'Euclidean') > 0 and Distance(a,O,'Sup') > 0 and Distance(a,O,'Manhattan') > 0 : # Positivity
				if Distance(a,c,'Euclidean') <= Distance(a,b,'Euclidean') + Distance(b,c,'Euclidean') and Distance(a,c,'Sup') <= Distance(a,b,'Sup') + Distance(b,c,'Sup') and Distance(a,c,'Manhattan') <= Distance(a,b,'Manhattan') + Distance(b,c,'Manhattan') : # Triangular inequality
					return True
				else :
					return False
			else :
				return False
		else :
			return False
	else :
		return False

######################################
# MAIN
######################################



def input_(string) : # Allows compatibility with Python 2 for input
	if sys.version_info[0] < 3 :
		return raw_input(string)
	else :
		return input(string)

def main(k,norm) :
	print("Starting programm...")
	print("Loading data...")
	dat = open('data.txt','r')
	data2 = dat.read().split("\n")
	dat.close()

	data = dict() # Every point is loaded into a dictionary
	i = 0
	for elt in data2 :
		if len(elt) != 0 :
			elt = elt.split(",")
			l = len(elt)-1
			data[len(data)] = point(i,elt[:l],elt[l])
			i+=1

	if k == "NULL" :
		maxi = len(data)
		k = 0
		while k == 0 :
			k = int(input_("Enter a number of group\n"))
			if k<1 and k>maxi:
				k=0

	print("Choosing "+str(k)+" centers...") # k centers are randomly chosen among the points
	centers = choose(k,data)

	print("Creating groups...") # And k empty groups are created according to the k chosen centers
	groups = make_group(centers, data)

	while norm == 'NULL' :
		norm = input_("Choose your norm for distance calculation: Euclidean, Manhattan or Sup\n")
		if norm != "Euclidean" and norm != "Manhattan" and norm != "Sup":
			norm = 'NULL'

	print(norm)
	print("Optimizing groups...")

	stable = False
	prestable = False

	while not stable : # As long as the centers are not stable, we optimize the groups (centers and associated points)
		centers_old = list(centers)
		groups = optimizing(groups,data,norm)
		groups,centers = new_centers(groups,centers,norm)
		for i in range(k) :
			stable = True
			if centers[i] != centers_old[i] :
				stable = False
			#print(centers,centers_old,stable)

	print("Groups optimized.")


	print("Verifying norms...")
	if verify_norms() :
		print("Norms successfully verified")
	else :
		print("An error has occured: norms do not behave correctly")

	print("Verifying results...")
	if verify_specie(groups) :
		print("Results successfully verified: all points in a group are of the same kind.")
	else :
		print("An error has been found: all points in a group are not of the same kind.")


	for group in groups :
		print("\n"+str(groups[group])+"\n")


	print("Done")

	return centers


main('NULL','NULL')

