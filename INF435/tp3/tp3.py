#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import graphviz
import diffusion
import measures
import k_cores
import random


## ----------------------------------
## Diffusion and centrality
## ----------------------------------



## --- GRAPH CONSTRUCTION ---

def create_node(listAdj, n_id):
	"""insert the node n_id in the adjacency list listAdj"""
	listAdj[n_id] = {}

def create_edge(listAdj, node1, node2, weight = 1.0):
	"""insert the edge linking two nodes node1 and node2"""
	listAdj[node1][node2] = weight
	listAdj[node2][node1] = weight



def get_k_nodes_degree(listAdj, k):

	# This will find the  most interesting nodes in the graph according to their degree

	deg = dict()

	for node in listAdj : # We calculate the degree of each node
		deg[node] = {}
		degree = 0
		for elt in listAdj[node]:
			if elt != 0 :
				degree += 1
		deg[node] = degree

	deg_sorted = list()	# And we keep only the k nodes of which the degree is the highest

	k_nodes = list()

	i = 0
	while i < k:
		MAX = 0
		NODE = 0
		deg_sorted += {0,0}
		for node in deg :
			if deg[node] > MAX:
				MAX = deg[node]
				NODE = node
		deg_sorted[i] = {NODE,MAX}
		del deg[NODE]
		i+=1
		k_nodes.append(NODE)

	return k_nodes
	#return mst_tree, core # Maximum Spanning Tree, final tree ?


def get_tree(listAdj, start_node, LIST):   # /!\ The current version has a huge memory issue /!\
	if start_node in listAdj :

		listAdj_updated = dict(listAdj)
		del listAdj_updated[start_node]

		for node in listAdj[start_node]:
			
			if len(LIST) == 0:
				LIST = [listAdj[start_node]]
			else :
				LIST+=get_tree(listAdj_updated,node,LIST)
		print(len(listAdj_updated),len(LIST))
		return LIST
	else :
		return []


def get_k_nodes_tree(listAdj, k):

	# This will find the most interesting nodes in the graph according to the size of their connected component

	tree = dict()


	for node in listAdj: #Need to analyse each sub graph
		tree[node] = {}
		print("node")
		tree[node] = get_tree(listAdj, node, [])

	print(tree['5'])
	print("haha")

	size = dict()

	for tre in tree: # Now we calculate the size of each sub graph
		size[tre] = {}
		siz = 0
		print('tre', tre)
		for node in tre:
			siz += 1
		size[tre] = siz

	print('size',size)	
	size_sorted = list() # And we keep the k nodes of which sub graphs have the maximum size

	k_nodes = list()

	i = 0
	while i < k:
		MAX = 0
		NODE = 0
		size_sorted += {0,0}
		for node in size :
			if size[node] > MAX:
				MAX = size[node]
				NODE = node
		size_sorted[i] = {NODE,MAX}
		del size[NODE]
		i+=1
		k_nodes.append(NODE)

	print("hoho")

	return k_nodes

	#return mst_tree, core # Maximum Spanning Tree, final tree ?


## --- MAIN ---
		
if __name__ == "__main__":
	random.seed()
	listAdj = {}
			
	## The graph is described in a file
	## There are three configurations:

	## For the promotion graph
	#filename="promotion.graph"
	#k = 7
	#start_node = 'Valjean'

	## For the dolphin graph
	filename="dolphin.graph"
	k = 3 
	#k = 5
	start_node = '1'

	## for a social network
	#filename = "socialnet.graph"
	#k = 7 
	#start_node = '1'

	## Display the graph
	graphviz.displayGraph(filename)
			
	fileGraph = open(filename, 'r')
	for line in fileGraph:
		line = line.strip()
		lineContent = line.split(" ")
		## retrieve id from file and create vertex
		if "id" in lineContent:
			ident = lineContent[1]
			create_node(listAdj, ident)
		## retrieve two ids from file and create edge between them
		if "edge" in lineContent:
			id1 = lineContent[1]
			if len(lineContent) == 4:
				id2 = lineContent[2]
				weight = float(lineContent[3])
				create_edge(listAdj, id1, id2, weight)
			else:
				id2 = lineContent[2]
				create_edge(listAdj, id1, id2)

	## ------------------------------------------------------------------------
	## 1. Calculate the rankings
	## ------------------------------------------------------------------------

	k_nodes = list()
	k_nodes2 = list()
	print("Trying the degree method...")
	k_nodes = get_k_nodes_degree(listAdj, 10)
	print("Result: ", k_nodes)
	print("Trying the extracted tree method...")
	k_nodes1 = get_k_nodes_tree(listAdj, 10)
	print("Result: ", k_nodes2)

	# k-cores
	kcores_result = k_cores.k_core_algorithm(listAdj, k, start_node)

	# To be fair and compare the metrics in the same conditions, recalculate k 
	# as the number of nodes in the connected core resulting in the last step of 
	# k_cores.k_core_algorithm 
	kcores = kcores_result[1].keys()
	k = len(kcores)
	print "new k = "+str(k)

	# pagerank
	pagerank		= measures.page_rank(listAdj)
	best_pagerank	= measures.select_best_k(pagerank, k)
	worst_pagerank	= measures.select_worst_k(pagerank, k)

	# Insert here the call to your methods


	## ------------------------------------------------------------------------
	## 2. Try the diffusion models
	## ------------------------------------------------------------------------
	print "kcores : %s" % kcores
	diff_result = diffusion.independent_cascade(listAdj, kcores)
	activated_nodes = diff_result[0]
	print "kcores => activated_nodes after IC : %s" % activated_nodes
	graphviz.show_active_nodes(kcores, activated_nodes, filename, "IC_kcores")

	diff_result = diffusion.linear_threshold(listAdj, kcores, 0.2)
	activated_nodes = diff_result[0]
	print "kcores => activated_nodes after LT : %s" % activated_nodes
	graphviz.show_active_nodes(kcores, activated_nodes, filename, "LT20_kcores")

	print "best_pagerank : %s" % best_pagerank
	diff_result = diffusion.independent_cascade(listAdj, best_pagerank)
	activated_nodes = diff_result[0]
	print "best_pagerank => activated_nodes after IC : %s" % activated_nodes
	graphviz.show_active_nodes(
			best_pagerank, activated_nodes, filename, "IC_best_pagerank")
		
	diff_result = diffusion.linear_threshold(listAdj, best_pagerank, 0.55)
	activated_nodes = diff_result[0]
	print "best_pagerank => activated_nodes after LT : %s" % activated_nodes
	graphviz.show_active_nodes(
			best_pagerank, activated_nodes, filename, "LT55_best_pagerank")	

	# Test here the diffusion from the k influencers found with your methods

	## ------------------------------------------------------------------------
	## 3. Experiment and compare the measures and diffusion models performances
	## ------------------------------------------------------------------------
	print "\n"
	print "---- Set of algorithms using the independent cascade as a diffusion model ----"
	
	print "-- k-core"
	result_b = diffusion.independent_cascade_experiment_generator(listAdj, kcores)
	print "Percentage of active nodes for IC+k core: %s (%f)" \
			% (result_b['diffusion_rate'][0], result_b['diffusion_rate'][1])
	print "Diffusion speed for IC+k core: %s (%f)" \
			% (result_b['diffusion_speed'][0], result_b['diffusion_speed'][1])

	print "\n\n-- page rank"
	result_b = diffusion.independent_cascade_experiment_generator(listAdj, best_pagerank)
	result_w = diffusion.independent_cascade_experiment_generator(listAdj, worst_pagerank)
	print "Percentage of active nodes for IC+PR: %s (%f)" % (result_b['diffusion_rate'][0], result_b['diffusion_rate'][1])
	print "Diffusion speed for IC+PR: %s (%f)" % (result_b['diffusion_speed'][0], result_b['diffusion_speed'][1])
	print "\nPercentage of active nodes for IC+(bad)PR: %s (%f)" % (result_w['diffusion_rate'][0], result_w['diffusion_rate'][1])
	print "Diffusion speed for IC+(bad)PR: %s (%f)" % (result_w['diffusion_speed'][0], result_w['diffusion_speed'][1])

	# Evaluate here the efficiency of your measures

	print "DONE!!"
