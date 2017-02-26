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
This software implements a k-means algorithm. Data must be written in a file named 'data.txt' as follow : coord1, coord2, ..., coordn, string\ncoord1', ...
It will be possible to choose between different types of norm calculation - Euclidean and Manhattan are currently available.

There is two classes : point and group. A point is defined by its name (id), its coordinates and a string (for instance, its specie). A group is defined by a name (id), a center (point), and points.
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


class group :
	def __init__(self,name) :
		self.name = name
		self.center = None
		self.points = list()
		return

	def center(self, center) :
		self.center = center
		return
	
	def add(self,point) : # /!\ DOES NOT SEEM TO WORK /!\
		self.points.append(point)
		return

	def remove(self,point) : # /!\ DOES SEEM TO WORK, AT LEAST PARTIALLY /!\
		#if self.center == point :
		#	self.center = self.points[0]
		self.points.remove(point)
		return

	def __str__(self) :
		s = str()
		for point in self.points :
			s += " "+str(point)
		return str(self.name) + " : " + str(self.center) +" : " + s


######################################
# DISTANCE CALCULATION
######################################



def Euclidean(center, point):
	# center is a point type and is the reference, point is a point type

	tmp = 0
	l = len(center.coordinates)-1

	for i in range(0,l) :
		tmp+=(float(center.coordinates[i])-float(point.coordinates[i]))**2

	return math.sqrt(float(tmp))



def Manhattan(center, point) :
	tmp = 0
	l = len(center.coordinates)-1
	for i in range(0,l) :
		tmp += abs(float(center.coordinates[i])-float(point.coordinates[i]))
	return tmp


#####################################
# INITIALIZATION
#####################################

def choose(k,data) :
	centers = list()
	i = 0
	while i < k :
		tmp = random.randrange(len(data))
		if tmp not in centers :
			centers.append(tmp)
			i+=1
	return centers

def make_group(centers,data) :
	# Builds the initial groups with their centers only
	groups = dict()
	i = 0
	for elt in centers :
		Group = group(str(i))
		Group.center = data[elt]
		groups[i] = Group
		i+=1
		#print(Group)
	return groups

######################################
# LOOP INSTRUCTIONS
######################################

def optimizing(groups,data) :
	# Calculates the distance of every point to every centers and optimizes groups
	for point in data : # Calculates the distances
		dist = list()
		for group in groups :
			dist.append(Euclidean(groups[group].center,data[point]))
		i = 0
		mini = dist[0]
		for elt in dist : #Finds the closest center and group
			if elt <= mini :
				mini = elt
				gr = i
			i+=1
		if point not in groups[gr].points : # Changes group if needed
			groups[gr].add(data[point])
			print("point added")
		for group in groups : # Removes the point from its previous group if needed
			if groups[group].name != gr and data[point] in groups[group].points and groups[group].center != data[point] :
				groups[group].remove(data[point])
				print("point removed")
			print(groups[group])
	return groups



def new_centers(groups,centers) :
	# Calculates the centers of the different groups
	for group in groups : #Calculates the barycenter of every group
		bary = [0]
		gr = groups[group]
		for point in gr.points :
			i = 0
			print(gr)
			p = point
			print(p)
			for coordinate in p.coordinates :
				if len(bary)-1 < i :
					bary.append(float(coordinate))
				else :
					bary[i] += float(coordinate)
				i+=1
		coordinates = list()
		for coordinate in bary :
			coordinates.append(float(coordinate)/float(len(gr.points)))
		)
		barycenter = point("bary"+str(group),coordinates," ") # /!\ DOES NOT SEEM TO WORK /!\
		for point in gr.points :
			dist = list()
			dist.append(Euclidean(barycenter,point))
		dmin = dist[0]
		for i in dist :
			if d < dmin :
				dmin = d
				b = i
			i+=1
		centers2.append(gr.points[b])
		gr.center = gr.points[b]

	return groups,centers2


######################################
# TESTS
######################################


def verify(groups) : # Verifies that every points in the same group have the same specie
	return True


######################################
# MAIN
######################################


def input_(string) : # Allows compatibility with Python 2
	if sys.version_info[0] < 3 :
		return raw_input(string)
	else :
		return input(string)


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
		#print(data[i])
		i+=1

print("Data loaded.")





maxi = len(data)
k = 0
while k == 0 :
	k = int(input_("Enter a number of group\n"))
	if k<1 and k>maxi:
		k=0

print("Choosing "+str(k)+" centers...") # k centers are randomly chosen among the points
centers = choose(k,data)
print(str(k)+" centers chosen.")

print("Creating groups...") # And k empty groups are created according to the k chosen centers
groups = make_group(centers, data)


for group in groups :
	print(groups[group])




print("Optimizing groups...")

stable = False

while not stable : # As long as the centers are not stable, we optimize the groups (centers and associated points)
	
	for group in groups :
		print(groups[group])
	groups = optimizing(groups,data)
	groups,centers = new_centers(groups,centers)
	for i in range(k) :
		stable = True
		if centers[i] != centers2[i] :
			stable = False

print("Groups optimized.")

print("Done")



