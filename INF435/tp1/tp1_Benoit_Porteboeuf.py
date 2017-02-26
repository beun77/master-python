#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import graphviz

## ----------------------------------
## TP1
## ----------------------------------



## --------------------------
## --- GRAPH CONSTRUCTION ---
## --------------------------


def create_node(listAdj, node_id):
	""" 
	Insert the node in the data structure
	Paramters:
		listAdj: the adjacency list, represented in a dictionnary indexed on node ids
		node_id: the name/id of the new node
	"""
	listAdj[node_id] = []
	return


def create_edge(listAdj, node1, node2):
	""" 
	Insert the edge linking two nodes 'node1' and 'node2' in the data structure 
	Parameters:
		listAdj: the adjacency list, represented in a dictionnary indexed on node ids
		node1, node2: the ids of the nodes linked by the new edge
	"""
	if node1 in listAdj and node2 in listAdj:
		listAdj[node1].append(node2)
		listAdj[node2].append(node1)
	return
		



## -----------------------------------------------------
## --- Search components and find the best source(s) ---
## -----------------------------------------------------


# This is a recursive function that looks for the immediate neighbours of a given node

def neighbours(listAdj, node1) :

	if node1 in listAdj:
		neig = list()
		neig2 = list()

		for elt in listAdj[node1] :
			neig.append(elt)
			neig2.append(elt) 
			
		del listAdj[node1]		

		for e in neig:
			neig2 += neighbours(listAdj, e)

		return neig2
	else:
		return []

# This is a recursive function that looks for immediate neighbours and calculate the score

def neighbours_and_score(listAdj, node1, score, neig3) :

	if node1 in listAdj:
	
		neig = list()
		neig2 = list()


		score += 1
		for elt in listAdj[node1] :
			neig.append(elt)
			neig2.append(elt)
		neig3[score] = neig2 
		del listAdj[node1]		

		for e in neig :
			tmp = neighbours_and_score(listAdj, e, score, neig3)
		
		neig3[score] = neig2
		return neig3 
	else:
		return {} 


def search_components(listAdj):
	""" 
	Find the connected components in listAdj. 
	Parameter:
		listAdj: the adjacency list, represented in a dictionnary indexed on node ids
	Return:
		the number of connected components, and 
		a dictionnary describing the components. E.g for disconnected-robot.graph, 
			the components are {
				1: ['A', 'C', 'B', 'D'], 
				2: ['E', 'F', 'G'], 
				3: ['H', 'I']
			}
	"""
	components_count = 0
	components = {}

	## TODO Insert your code here


	listAdj_copy = dict(listAdj)


	components_count = 0

	# We make sure that every node is analyzed

	while len(listAdj_copy) > 0 :
		for node in listAdj :

			# ListAdj is compared to ListAdj_copy so that every node is analyzed exactly one time
			if node in listAdj_copy :
				print(listAdj_copy[node])

				# We have now entered a connected component and we use a recursivity function
				components[components_count] = neighbours(listAdj_copy, node)

				# ListAdj_copy is updated
				for e in components[components_count]:
					if e in listAdj_copy :
						del listAdj_copy[e]
				components_count += 1
			
	return components_count, components
	

def score(listAdj, node1):
	"""
	Find the shortest paths between a node node1 and all the other nodes in the 
	same component. Compute the score as the cost (length) of the paths (as the 
	graph is not valued, each edge traversal costs "1")

	Parameter:
		listAdj: the adjacency list, represented in a dictionnary indexed on node ids
		node1: the original position of the robot
		
	Return:
		the score of node1, 0 if node1 is an isolated node
	"""
	
	## TODO Insert your code here
	sco = 0	

	node_found = dict()

	listAdj_copy = dict(listAdj)
	node_found = dict(neighbours_and_score(listAdj_copy, node1, 0, {}))
	
	
	done = dict()

	for elt in node_found :
		for el in node_found[elt] :
			if el not in done  :
				done[el] = elt
	for elt in done :
		sco += done[elt]

	return sco


 
## ------------
## --- MAIN ---
## ------------

if __name__ == '__main__':
	# Note: "if __name__ == '__main__':" is the standard main syntax in python. 
	# Don't wonder too much about it, just know that the main is inside this block.

	# The graph is described in a file
	filename="robot.graph"
	#filename="disconnected-robot.graph"

	# a hash-table for the edges : {node1 : [node3, node4], ...} if node 1 is 
	# linked to 3 and 4, etc. The robot.graph is listAdj = { 
	#	 'A': ['C'], 
	#	 'C': ['A', 'B', 'D', 'E'], 
	#	 'B': ['C'],  
	#	 'E': ['C', 'F'], 
	#	 'D': ['C'],  
	#	 'G': ['F', 'H', 'I'], 
	#	 'F': ['E', 'G'],  
	#	 'I': ['G', 'H'], 
	#	 'H': ['G', 'I']  }
	listAdj = {}

	# Display the graph: Creates a filename.png file. Check it up!
	graphviz.displayGraph(filename)
		
	# Read the graph file, and fill the data structure. 
	fileGraph = open(filename, 'r')
	for line in fileGraph:
		# Check the doc of str.strip() and str.split() to understand!
		lineContent = line.strip().split(" ")

		## retrieve node id from file and create node
		if "id" in lineContent:
			node_id = lineContent[1]
			create_node(listAdj, node_id)
			
		## retrieve two ids from file and create edge between them
		if "edge" in lineContent:
			id1 = lineContent[1]
			id2 = lineContent[2]
			create_edge(listAdj, id1, id2)


	print "\nThe adjacency list storing the graph:"
	print listAdj
	print "\n==========================\n"


	# Search the number of connected componentsa (stored in components_count)
	# components is a dictionnary to store sub-graphs (nodes repartition into 
	# connected components). For disconnected-robot.graph, the components are 
	# {1: ['A', 'C', 'B', 'D'], 2: ['E', 'F', 'G'], 3: ['H', 'I']}

	# TODO: fill the body of search_components
	components_count, components = search_components(listAdj)  

	print "The number of connected components is :", components_count
	print "Sub-graphs in each component :", components
	print "\n==========================\n"

	# For each component, find the best source. 
	for component_id, nodes in components.items():
		print "\n***** Compute the best source node for component ", component_id
		best_source = ""
		best_score = None
		for source in nodes:
			# score() is empty, you have to fill it!
			thescore = score(listAdj, source)
			print "Score for source ", source, ": ", thescore
			if best_score == None or thescore < best_score:
				best_source = source
				best_score = thescore
		print "Best source: %s (score %d)" % (best_source, best_score)


