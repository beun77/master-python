#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

## ----------------------------------
## TP2 
## ----------------------------------

import graphviz

## ----------------------------------
## global variables and data structure





## ----------------------------------
## --- GRAPH CONSTRUCTION ---

##
## vertex creation

def createVertex(id):
    """insert the vertex in your data structure"""
    
    print(id)

##
## edge creation

def createEdge(listAdj, node1, node2, value):
	"""insert the edge linking two vertices 'node1' and 'node2' in your data structure

	don't forget to add the 'friendship value' !!!
	Parameters:
		listAdj: the adjacency list, represented in a dictionnary indexed on node ids
		node1, node2: the ids of the nodes linked by the new edge
	"""
	if not (node1 in listAdj) :
		listAdj[node1] = {}
	if not (node2 in listAdj) :
		listAdj[node2] = {}

	listAdj[node1]={node2, value}#.append({node2, value})
	listAdj[node2]={node1,value}#.append({node1, value})

	print node1, "<---"+value+"--->", node2

	return listAdj

## ----------------------------------
## --- PART  "Diffusion" ---
##
## create the cheapest broadcast tree

# This is a recursive function that looks for the immediate neighbours of a given node

def neighbours(listAdj, node1) :

	listAdj_copy = list(listAdj)

	# This is a recursive function that finds all the neighbours of a given node

	neig = list()
	neig2 = list()

	for elt in listAdj_copy :
		el = list(elt)
		if el[0] == node1 :
			neig.append(el[1])
		elif el[1] == node1 :
			neig.append(el[0])
		
	# We update listAdj_copy

	for elt in neig :
		for el in listAdj_copy :
			e = list(el)
			if elt == e[0] or elt == e[1] :
				listAdj_copy.remove(el)

	neig2 = list(neig)

	if len(neig) > 0 :
		for e in neig :
			neig2 += neighbours(listAdj_copy, e)
		return neig2
	else :
		return []
"""
	listAdj_copy = dict()

	# Convertion of a list into a dictionary

	i = 0
	for elt in listAdj :
		elt = list(elt)
		listAdj_copy[elt[0]] = elt[1]
		listAdj_copy[elt[1]] = elt[0]
		if elt[0] != node1 and elt[1] != node1 :
			i+=1

	if node1 in listAdj_copy:
		neig = list()
		neig2 = list()

		for elt in listAdj_copy[node1] :
			neig.append(elt[0])
			neig2.append(elt[0]) 
			
		#del listAdj_copy[node1]		

		del listAdj[i]

		for e in neig:
			neig2 += neighbours(listAdj, e)
		print("haha")
		return neig2
	else:
		return []
"""


def is_connected(listAdj):

	listAdj_copy = list(listAdj)

	components = list()
	components_count = -1

	# We make sure that every node is analyzed

	while len(listAdj_copy) > 0 :
		for node in listAdj :
			# ListAdj is compared to ListAdj_copy so that every node is analyzed exactly one time
			for nde in listAdj_copy :
				if node == nde :
					node = list(node)
					#print("in a connected component")
					# We have now entered a connected component and we use a recursivity function
					#print('node',node)	
					#print('components',components, 'node', node, 'components_count', components_count)
					"""if len(components) == 0 :
						components = neighbours(listAdj_copy, node[0])
					else :
						components[components_count] = neighbours(listAdj_copy, node[0])
					"""
					components.append(neighbours(listAdj_copy, node[0]))

			if len(components) > 0 :
				# ListAdj_copy is updated
				for elt in components : # Different possible connected components
					for el in elt : # Different nodes in a connected component
						for e in listAdj_copy : # Different node in a pair of nodes
							E = list(e)
							if el == E[0] or el == E[1] :
								#del listAdj_copy[e]
								listAdj_copy.remove(e)
					components_count += 1

				#print("out of a connected component")

	if components_count > 1 :
		return False
	else :
		return True


def get_key(item) :
	return item[1]


def cheapestTree(listAdj) : #(node="Babet"):
	"""return the 'overall friendship cost' and the set of edges

	result is (an integer, a list of pair of nodes)
	"""    
	# We propose a version of Kruskal algorithm in order to find the maximum spanning tree

	edge = list()

	# We stock all edges in a list

	for elt in listAdj :
		el = sorted(list(listAdj[elt]), reverse = True)
		edge.append([elt, el[0], el[1]])
	#print("edge", edge)

	# We now sort them according to their weight
	edge_sorted = sorted(edge, key=get_key, reverse = True)

	# And we eliminate doubles

	edge_sorted_final = list(edge_sorted)
	for elt in edge_sorted :
		for el in edge_sorted_final :
			if elt[0] == el[1] and elt[1] == el[0] and elt[2] == el[2] :
				edge_sorted_final.remove(el)

	# Finally, we now build our maximum spanning tree
	tree = list()
	total_cost = 0
	
	#print("no double", edge_sorted_final)

	for elt in edge_sorted_final :
		tree_tmp = list(tree)
		tree_tmp.append({elt[0],elt[1]})
		print(elt[2], tree, tree_tmp)
		if len(tree) == 0 :
			tree = list(tree_tmp)
			total_cost += int(elt[2])
			print("haha")
		elif is_connected(tree) == False :
			tree = list(tree_tmp)
			total_cost += int(elt[2])
			print("hoho")
		else :
			print("hihi")
	return (total_cost, tree)
    
## ----------------------------------
## --- PART  "Diffusion paths" ---
##
## create all the possible path to any node from any node


def diffusionPaths(tree):
    """return for each "source_target" the sequence of nodes composing the path
    
    result is a dictionnary {'Mabeuf_Cosette': ['Mabeuf', 'Marius', 'LtGillenormand', 'Cosette'], 'Mabeuf_Valjean': ['Mabeuf',...,'Valjean'], ...}
    """    
    
    return {}


## ----------------------------------
## --- PART "Optimisation" ---
##
## find the better root

def bestRoot(tree):
    """return the node so that the tree depth is minimal
    
    'tree' is a list of pair of nodes
    """
    
    return ""
    

    
## ----------------------------------
## ----------------------------------
## ----------------------------------
## --- MAIN ---

    
fileGraph = open("promotion.graph", 'r')
listAdj = dict()
for line in fileGraph:
    
    lineContent = line.split(" ")

    ## retrieve id from file and create vertex
    if "id" in lineContent:
        ident = lineContent[1][:-1]
        createVertex(ident)
        
    ## retrieve two ids and a value from file and create edge between them
    if "edge" in lineContent:
        id1 = lineContent[1]
        id2 = lineContent[2]
        weight = lineContent[3][:-1]
        listAdj = createEdge(listAdj, id1, id2, weight) ## This crerateEdge is empty !!!!!!
## test the PART  "Diffusion"
res = cheapestTree(listAdj)
graphviz.showcheapestTree(res) # show the tree: blue edges
print
print "The 'overall cost' is", res[0]
print "Here is the set of communication links to create: "
for edge in res[1]:
    print str(edge[0])+" --- "+str(edge[1])
    
## Store all the possible paths from any source to any target
## The expected Gpath could be this way:
## Gpath = {'Mabeuf_Cosette': ['Mabeuf', 'Marius', 'LtGillenormand', 'Cosette'], 'Mabeuf_Valjean': ['Mabeuf',...,'Valjean'], ...}
Gpath=diffusionPaths(res[1])
if 'Mabeuf_Cosette' in Gpath.keys():
	print
	print "The path Mabeuf -> Cosette is ", Gpath['Mabeuf_Cosette']

    
## test the PART "Optimisation"
print
print "The best root is", bestRoot(res[1])


