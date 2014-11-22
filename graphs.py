#####################################################################################
# graphs.py
# some helpers for manipulating and defining graphs
#####################################################################################

import sys, math, numpy
import networkx as nx
import matplotlib.pyplot as plt

#####################################################################################
# CONVERT GRAPH REPRESENTATION BETWEEN ADJACENCY MATRIX AND LIST
#####################################################################################
# matrixToList(A): 
# given the adjacency matrix of a graph, returns its adjacency list
#####################################################################################
def matrixToList(A):
	[num_rows, num_cols] = A.shape
	assert num_rows == num_cols

	G = []
	for j in range(num_rows):
		for k in range(num_cols):
			if A[j][k] != 0:
				G.append([j,k])

	return G

#####################################################################################
# listToMatrix(G): 
# given the adjacency list of a graph, returns its adjacency matrix
#####################################################################################
def listToMatrix(G):

	vertices = set([v1 for v1,v2 in G] + [v2 for v1,v2 in G])
	n = len(vertices)
	A = numpy.zeros(shape = (n,n))

	for j in range(n):
		for k in range(n):
			if [j,k] in G:
				A[j,k] = 1

	return A


#####################################################################################
# GRAPH DRAWING AND LAYOUT GENERATION (PYTHON NETWORKX LIBRARY)
#####################################################################################
# draw_graph(G): 
# graph drawing of G 
# source: networkx example code
#####################################################################################
def draw_graph(graph):

	# extract nodes from graph
	nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

	# create networkx graph
	G=nx.Graph()

	# add nodes 
	for node in nodes: 
		G.add_node(node)

	# add edges 
	for edge in graph: 
		G.add_edge(edge[0], edge[1])

	# draw graph 
	pos = nx.shell_layout(G) 
	print "Pos = ", pos 
	nx.draw(G, pos)

	# show graph
	plt.show()


#####################################################################################
# place_graph(G): 
# given a graph G, return a list of 2d positions for all vertices 
#####################################################################################
def place_graph(graph):

	# extract nodes from graph
	nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

	# create networkx graph
	G=nx.Graph()

	# add nodes
	for node in nodes:
		G.add_node(node)

	# add edges
	for edge in graph:
		G.add_edge(edge[0], edge[1])

	# compute placements
	pos = nx.shell_layout(G)
	return pos
    


#####################################################################################
# GENERATE SOME STANDARD GRAPHS
#####################################################################################
# pathGraph(n):
#####################################################################################
def pathGraph(n):
	A = numpy.zeros(shape = (n,n))

	for i in range(n):
		for j in range(n):
			if abs(i-j) == 1:
				A[i][j] = 1.0

	return A

#####################################################################################
# cycleGraph(n):
#####################################################################################
def cycleGraph(n):
	A = numpy.zeros(shape = (n,n))

	for i in range(n):
		for j in range(n):
			if pow(i-j,1,n) == 1:
				A[i][j] = 1.0

	return A

#####################################################################################
# clique(n): 
# returns the adjacency matrix of the complete graph on n vertices
#####################################################################################
def completeGraph(n):
	A = numpy.zeros(shape = (n,n))

	for i in range(n):
		for j in range(n):
			if i != j:
				A[i][j] = 1.0

	return A

#####################################################################################
# completeOrientedGraph(n): 
# returns the adjacency matrix of the complete oriented graph on n vertices
#####################################################################################
def completeOrientedGraph(n):
	A = (numpy.zeros(shape = (n,n))).astype(complex)

	for p in range(n):
		for q in range(n):
			if q == n-1 and p == 0:
				A[p][q] = 0+1j
			elif q < p:
				A[p][q] = 0+1j
			else:
				if p != q:
					A[p][q] = 0-1j

	return A


