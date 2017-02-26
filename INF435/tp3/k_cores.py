# -*- coding: iso-8859-15 -*-

import heapq
import random
from numpy import Infinity
from measures import degree


"""
This file contains the implementation of the k-cores algorithm, first 
introduced in:

Spread of Information in a Social Network Using Influential Nodes, Arpan 
Chaudhury, Partha Basuchowdhuri and Subhashis Majumder, PAKDD 2012, Part II, 
LNAI 7302, pp. 121–132, 2012.
"""

def k_core_algorithm(listAdj, k, start_node ):
	"""
	k-core algorithm

	k: the k highest degree nodes
	start_node: the starting point for the MST algorithm

	Returns: the mst spanning tree (adjacency list) and the core.
	"""

	print "-----"
	print "Results of k-core algorithm"
	print "-----"
	print 

	# 1. Revise the weights, and calculate the iso-graph
	rev_iso_graph_listAdj = revised_weight_iso(listAdj)

	# 2. Compute the minimal spanning tree of rev_iso_graph
	mst_tree, cost = prim_MST(rev_iso_graph_listAdj, start_node)
	print "Maximal spanning tree (cost=%d):\n%s\n" % (cost, mst_tree)

	# 3. Select k nodes from the mst. These nodes should have a degree higher 
	# than some threshold. As we don't know how to compute this threshold, we 
	# will select just the k node with the higer degree (Lines 3-8)
	vc = get_k_highest_degree(listAdj, k)
	print "k=%d most interesting nodes: %s\n" % (k, vc)

	# 4. Extract the core network (Lines 9-13)
	ec = extract_core( mst_tree, vc )

	# 5. The network can be disconnected... use DFS to find the components
	vcc = DFS_components(ec)
	print "%d component(s) in the core\n" % (len(vcc))

	# 6. Reconnect the components...
	core = reconnect_components(mst_tree, vcc)
	print "Reconnected core: %s\n" % (core)
	return  mst_tree, core


def revised_weight_iso(listAdj):
	"""
	Function for calculating the revised weight according to equation 3 and the
	iso-graph (the graph with negative weights)

	Returns iso_graph_listAdj, which is equivalent to listAdj, with all weights  
	multiplied by -1
	"""
	rev_iso_graph_listAdj = {}
	for source in listAdj:
		rev_iso_graph_listAdj[source] = {}
		source_degree = degree(listAdj, source)
		for neigh in listAdj[source]:
			neigh_degree = degree(listAdj, neigh)
			rev_iso_graph_listAdj[source][neigh] = -0.5 * \
					listAdj[source][neigh] * (source_degree + neigh_degree)
	return rev_iso_graph_listAdj


def prim_MST(listAdj, start_node):
	"""
	Prim's minimal spaning tree algorithm

	This implementation is probably fairly different from what you've used in 
	Lab2: it uses priority queues, thanks to the heapq library. See 
	documentation (pydoc heapq)

	Return mst, which has the same adjacency list shape as the one in Lab1.
	"""
	node_queue	= []	# Contains pairs of (cost, node), for the nodes that 
						# still need to be added in the MST
	keys		= {}	# Indexed on nodes: the cost to add the node in the MST
	predecessor	= {}	# Indexed on nodes: the predecessor of the node

	mst = {start_node: [], }
	visited = [start_node, ]
	total_cost = 0
	
	initialize_single_source(listAdj, start_node, node_queue, keys)

	while node_queue:
		# Extract min
		cost, node = heapq.heappop(node_queue)
		total_cost += cost
				
		visited.append(node)
		if node != start_node:
			mst[node] = []
			mst[predecessor[node]].append(node)
			mst[node].append(predecessor[node])

		for neigh in listAdj[node]:
			# pseudo-relax
			candidate_key = listAdj[node][neigh]
			if neigh not in visited and candidate_key < keys[neigh]:
				keys[neigh] = candidate_key
				update_node_queue(node_queue, neigh, candidate_key)
				predecessor[neigh] = node

	return mst, total_cost



def initialize_single_source(listAdj, start_node, node_queue, keys):
	for node in listAdj:
		if node == start_node:
			keys[node] = 0.0
		else:
			keys[node] = Infinity
		heapq.heappush(node_queue, (keys[node], node))
	heapq.heapify(node_queue)


def update_node_queue(node_queue, node, new_key):
	"""
	Updates the min priority queue with the new key value. Remember, in this 
	step, the given key should be smaller than the original
	"""
	# 1. Find the node
	i = 0
	while i < len(node_queue) and node_queue[i][1] != node:
		i += 1
	
	# 2. If it was found, update the key
	if i < len(node_queue):
		node_queue[i] = (new_key, node)
		heapq.heapify(node_queue)


def get_k_highest_degree(listAdj, k):
	"""
	Finds vc: the k nodes with the highest degree 
	Uses a heap to sort the nodes according to their degree 	 
	"""
	vc			= []
	sorted_deg	= []	# Priority queue, contains (degree, node) pairs. Since 
						# the priority goes to the item with the lowest key, 
						# the degrees are multiplied by -1

	# Create and fill the heap
	for node in listAdj:
		sorted_deg.append((-degree(listAdj, node), node))
	heapq.heapify(sorted_deg)
	
	if k >= len(sorted_deg):
		k = len(sorted_deg)
	for i in xrange(k):
		vc.append(heapq.heappop(sorted_deg)[1])
	return vc


def extract_core(tree, vc):
	"""
	Using the core nodes (vc), select the corresponding edges in the mst (tree)

	Returns an adjacency list ec, containing the edges of tree that link nodes 
	from vc.
	"""
	ec = {}
	for node in tree:
		if node in vc:
			ec[node] = []
			for neigh in tree[node]:
				if neigh in vc:
					ec[node].append(neigh)
	return ec


def DFS_components(ec):
	"""
	Performs a DFS to find connected components in the core ec.
	This is not a recursive implementation of DFS: it uses a stack (last in, 
	first out), which is the opposite of queue (first in, first out)
	
	Returns a dictionary with the list of nodes of each component
	"""
	vcc = {}
	visited = []	
	comp_count = 0
	for node in ec:
		if node not in visited:
			# Beginning of a new component
			node_stack = [node, ]
			vcc[comp_count] = {}
			while node_stack:
				next_node = node_stack.pop()
				if next_node not in vcc[comp_count]:
					visited.append(next_node)
					vcc[comp_count][next_node] = []
					for neigh in ec[next_node]:
						if neigh not in visited and neigh not in node_stack:
							node_stack.append(neigh)
							vcc[comp_count][next_node].append(neigh)
				else:
					assert False
			comp_count += 1
	return vcc


def get_geodesic_shortest_path(listAdj, node1, node2):
	"""
	Use BFS to find the (shortest geodesic) path between node1 and node2. 
	If listAdj is a tree, this path is the only path. 

	Returns the path, and the distance between the nodes
	"""
	path		= []
	distance	= Infinity
	
	visited		= []
	to_visit	= []
	predecessor	= {}
	
	found = False
	to_visit.append(node1)
	while to_visit and not found:
		current_node = to_visit.pop(0)
		if current_node == node2:
			found = True
		else:
			for neigh in listAdj[current_node]:
				if neigh not in visited and neigh not in to_visit:
					to_visit.append(neigh)
					predecessor[neigh] = current_node
			visited.append(current_node)

	if node2 in predecessor:
		current = node2
		distance = 0
		while current != node1:
			path.insert(0, current)
			current = predecessor[current]
			distance += 1
		path.insert(0, current)
		distance += 1
	return path, distance


def get_all_paths(tree):
	"""
	Find all the paths between all pairs of nodes. For this, you should use the 
	MST since it contains the paths. The paths are stored within a structure of 
	the form "src_target: [src,n1,n2,...nk,target]"
	"""
	paths = {}
	for node1 in tree:
		for node2 in tree:
			# Check if the path node2->node1 was already seen
			inv_key = str(node2) + "_" + str(node1)
			if node1 != node2 and inv_key not in paths:
				key = str(node1) + "_" + str(node2)
				paths[key] = get_path(tree, node1, node2 )
	return paths




def get_path_between_components(tree, component_1, component_2):
	"""
	Find the path on the MST between the components (in the core)
	"""
	# Pick one node from each component
	node1 = random.choice(component_1.keys())
	node2 = random.choice(component_2.keys())

	# Get the path
	path, distance = get_geodesic_shortest_path(tree, node1, node2)

	# Remove unnecessary nodes: keep only one node from component_1 and one 
	# node from component_2.
	while path[1] in component_1:
		path.pop(0)
	while path[-2] in component_2:
		path.pop()
	return path

	
def reconnect_components(tree, components):
	"""
	Adds the required elements from the components or the MST or both to the 
	first component components[0], here called comp_0. 

	Returns an adjacency list: 
		comp_0: {node_a: [n1a, n2a, n3a], node_b: [n1b, n2b],...}
	"""
	while len(components) > 1:
		# Pick two components
		id1, id2 = random.sample(components.keys(), 2)

		# Merge components[id2] into components[id1]
		path = get_path_between_components(
				tree, components[id1], components[id2])
		i = 1	# i: index in path. Remark: path[0] always in components[id1]
		continue_exploration = True
		while continue_exploration and i < len(path):
			node = path[i]
			prevnode = path[i-1]
			if node in components[id1]:
				pass
			elif node in components[id2]:
				# id2 is reached. Merge it into components[id1]
				components[id1].update(components[id2])
				# add the missing edge
				components[id1][node].append(prevnode)
				components[id1][prevnode].append(node)
				continue_exploration = False
				del components[id2]
			else:
				for c_id in components.keys():
					if c_id != id1 and c_id != id2 and node in components[c_id]:
						# Path goes through a third component: merge it into 
						# components[id1], add the missing edge, remove the  
						# component.
						components[id1].update(components[c_id])
						components[id1][node].append(prevnode)
						components[id1][prevnode].append(node)
						del components[c_id]
						break 
				else:
					# This will be executed if the break statement is not hit, 
					# ie if node is not part of a component: then, add it to 
					# components[id1], and add the edge
					components[id1][node] = [prevnode, ]
					components[id1][prevnode].append(node)
			i += 1
	return components.values()[0]
					
