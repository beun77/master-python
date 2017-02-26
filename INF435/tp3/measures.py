# -*- coding: iso-8859-15 -*-

## ----------------------------------	
## ---------- PAGE RANK -------------
## ----------------------------------


def page_rank(listAdj, damping_factor=0.85, max_iterations=100, min_delta=1e-5):
	"""
	PageRank is the algorithm used to create the first version of the Google
	search engine. It is intended to be used on directed graph (the graph of 
	webpages, linked by hyperlinks). This implementation works also on directed 
	graphs.

	Returns a dictionary of the nodes and ranks of the form {node: rank, }

	Parameters:
	listAdj
	damping_factor: the probability that the surfer continues visiting nodes in 
		the graph. 
		1 - damping_factor is the probability that the surfer gets bored and 
		randomly jumps to another node (yeah, teleportation!) 
	max_iterations: a stoping criterion: the number of times the algorithm is 
		executed.
	min_delta: the minimum delta for which a new iteration is performed
	"""
	nb_nodes = len(listAdj)
	p_rank = {}
	if nb_nodes > 0:
		# The rank for nodes with no indegree: if the surfer arrives with a 
		# node with no indegree, he has to jump to another node
		min_value = (1.0 - damping_factor) / nb_nodes

		# At first, all the nodes have same probability
		p_rank = dict.fromkeys(listAdj.keys(), 1.0/nb_nodes)

		iteration = 0 
		continue_pr = True
		while iteration < max_iterations and continue_pr:
			diff = 0.0
			for node in listAdj:
				rank = min_value
				for in_neighbour in get_in_neighbours(listAdj, node):
					rank += (damping_factor * p_rank[in_neighbour] /
							len(listAdj[in_neighbour]))
				diff += abs(p_rank[node] - rank)
				p_rank[node] = rank
			continue_pr = (diff > min_delta)
			iteration += 1
	return p_rank
	

def select_best_k(node_rank, k):
	"""
	Generic function to select k nodes with the highest measure. The measure 
	can be calculated using page rank, centrality, betweennes, etc.

	Parameters:
	node_rank: dict indexed on nodes, associating each node with a measure
	k: number of nodes to select

	Returns:
	The selected k nodes
	"""
	sorted_list = sorted(node_rank.keys(),  
			key=lambda node: node_rank[node], reverse=True)
	if k > len(node_rank):
		k = len(node_rank)
	return sorted_list[:k]


def select_worst_k(node_rank, k):
	"""
	Generic function to select the k worst nodes for a givent measure. The 
	measure can be calculated using page rank, centrality, betweennes, etc.

	Parameters:
	node_rank: dictionnary indexed on nodes, associating each node with a 
		measure
	k: number of nodes to select

	Returns:
	The selected k nodes
	"""
	sorted_list = sorted(node_rank.keys(), 
			key=lambda node: node_rank[node], reverse=False)
	if k > len(node_rank):
		k = len(node_rank)
	return sorted_list[:k]
	

def degree(listAdj, node):
	"""
	Computes the degree of a node
	"""
	degree = 0
	if node in listAdj:
		degree = len(listAdj[node])
	return degree

	
def get_in_neighbours(listAdj, node ):
	"""
	Returns all the incoming neighbours of node.
	With a non directed graph, it is equivalent to the number of neighbours
	"""
	result = []
	for neighbour in listAdj:
		if node in listAdj[neighbour]:
			result.append(neighbour)
	return result
	

