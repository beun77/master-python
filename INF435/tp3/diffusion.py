# -*- coding: iso-8859-15 -*-

import random
import math
from numpy import mean, std


'''
!!!!!!!!! Read this before !!!!!!!!!

This file contains two diffusion models:
	- Independent cascade
	- Linear threshold

Each function in this file has the adjacency list as first parameter.	 
'''


## ----------------------------------	
## ------ DIFUSION ALGORITHMS --------
## ----------------------------------

def independent_cascade(listAdj, initial_active_nodes, p = 0.15):
	"""
	Independent cascade. In this diffusion method, each active node tries to 
	activate its neighbours. If successful, then the neighbour becomes active,
	otherwise the node cannot try to activate the same neighbour again.

	The algorithm stops when no new activation is registered during one step.

	Parameters:
	initial_active_nodes: List of the initially activated nodes 
	p: Contagion probability. Used to determine whether a noe activates one of 
		its neighbours. Note that if this probability p is set to be < 0, each 
		edge will have a random assigned probability 

	Returns the list of active nodes and the number of steps used
	"""

	active_nodes = [] + initial_active_nodes
	
	# Initialize the 'contagion' probabilities
	probabilities = generate_probabilities(listAdj, p)

	finished = False
	steps = 0
	while not finished:
		steps += 1
		finished = True
		for node in active_nodes:
			for neighbour in listAdj[node]:
				if neighbour not in active_nodes:
					proba = probabilities[node][neighbour]
					# Toss a coin to activate neighbour or not
					random_toss = random.random()

					if proba > random_toss:
						# Activate the neighbour
						active_nodes.append(neighbour)
						finished = False
					else:
						# Block the edge: set proba = 0: node cannot axtivate
						# neighbour anymore
						probabilities[node][neighbour] = 0.0
	return active_nodes, steps
	
def linear_threshold(listAdj, initial_active_nodes, threshold=0.3):
	"""
	Linear threshold diffusion model. This model propagates an information or 
	an opinion on a network. A given node will become active if the proportion 
	p of its active neighbours is equal or greater than threshold. 

	Parameters:
	listAdj
	initial_active_nodes: list with the initially activated nodes
	threshold: active neighbours / total neighbour count ratio necessary for 
		node activation

	Returns the list of active nodes and the number of steps used
	"""
	active_nodes = [] + initial_active_nodes
	
	finished = False
	steps = 0
	while not finished:
		steps += 1
		finished = True
		for node in active_nodes:
			for neighbour in listAdj[node]:
				if neighbour not in active_nodes:
					active_neighbourbours = 0
					total_neighbour = len(listAdj[neighbour])
					# Count neighbour's active neighbours
					for nneighbour in listAdj[neighbour]:
						if nneighbour in active_nodes:
							active_neighbourbours += 1.0
					# Compute ratio
					b = active_neighbourbours/total_neighbour
					if b >= threshold:
						# Node activation
						active_nodes.append(neighbour)
						finished = False
	return active_nodes, steps


############## START OF HELPER FUNCTIONS ##################

def generate_probabilities(listAdj, p = 0.15):
	"""
	Calculates the activation (or contagion) probabilities for each edge in the 
	network.

	Parameters:
	listAdj
	p: Contagion probability. If p >= 0, then the contagion probability is p 
		for each edge in the graph. Otherwise, it is set for each edge to a 
		random, uniformly distributed probability in range [0.0, 1.0).

	Returns a dictionary of the form {node: {neighbour1: p, neighbour2: p},...}
	"""
	probabilities = {}
	for node in listAdj:
		probabilities[node] = {}
		for neighbour in listAdj[node]:
			proba = p
			if p < 0.0:
				proba = random.random()
			probabilities[node][neighbour] = proba
	return probabilities
	

def activation_success(listAdj, activated_nodes):
	"""
	Calculate the proportion of active nodes
	"""
	return float(len(activated_nodes))/float(len(listAdj))
	

def independent_cascade_experiment_generator(listAdj, initial_nodes, 
		exp_size=40, p=0.15):
	"""
	Performs a number of experiments for the Independant Cascade (IC) model.

	Parameters:
	listAdj
	initial_nodes: the initially activated nodes
	exp_size: number of experiments to conduct
	p: the activation probability

	Returns a dictionary summarizing the diffusion performance (average and 
	standard deviation of the diffusion rate and speed)
	"""

	exp_result = []
	avg = 0.0
	i = 0

	# Run the experiments
	while i < exp_size:
		activated_nodes, steps = independent_cascade(listAdj, initial_nodes, p)
		act_success = activation_success(listAdj, activated_nodes)
		exp_result.append((act_success, steps))
		i += 1
	
	# Measure the average quality of the diffusion
	avg = mean(exp_result, 0)
	stddev = std(exp_result, 0)

	return {"diffusion_rate": (avg[0], stddev[0]), 
			"diffusion_speed": (avg[1], stddev[1])}
	

def linear_threshold_experiment_generator(listAdj, initial_nodes, 
		threshold=0.3):	
	"""
	Performs one experiment for the Linear Threshold model: it is deterministic

	Parameters:
	listAdj
	initial_nodes: the initially activated nodes
	p: the activation probability

	Returns a dictionary summarizing the diffusion performance (average and 
	standard deviation of the diffusion rate and speed)
	"""
	active_nodes, steps = linear_threshold(listAdj, initial_nodes, threshold)
	act_success = activation_success( tabNode, active_nodes )

	return {"diffusion_rate": act_success,  "diffusion_speed": steps}

