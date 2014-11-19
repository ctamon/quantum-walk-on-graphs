import pygame, sys, math, cmath, numpy
from pygame.locals import *

from qtools import *
from graphs import *

# some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
	
# graphics (display/layout) parameters
WINDOWSIZE = 600
GRAPHSIZE = WINDOWSIZE/2
MY_RADIUS = 30
MY_THICKNESS = 5

############################################################################
# qwalk_me(A)
# given a graph G defined by an adjacency matrix A,
# simulate a quantum walk (running indefinitely) on G
############################################################################
def qwalk_me(A):
	# switch graph from matrix to list
	G = matrixToList(A)

	[num_rows, num_cols] = A.shape
	assert num_rows == num_cols

	# compute placement of vertices (in the 2d layout)
	hashes = place_graph(G)	

	nokeys = [b for a,b in hashes.items()]

	positions = map(lambda x: x.tolist(), nokeys)
	
	def scale(x): return int(x*(GRAPHSIZE/2) + (WINDOWSIZE/2))

	Vertex = map(lambda p: (scale(p[0]), scale(p[1])), positions)

	# circle layout of a vertex
	radius = MY_RADIUS 
	thickness = MY_THICKNESS

	# start time for quantum walk
	current_time = 0
	delta_time = 0.01

	# initialize vertex colors
	my_color = [0 for i in range(num_rows)]
	
	# initialize vertex amplitudes and probabilities
	ampl = [(1.0 if i == 0 else 0.0) for i in range(num_rows)]
	prob = [(1.0 if i == 0 else 0.0) for i in range(num_rows)]

	# setup the graphics
	pygame.init()

	FPS = 30
	fpsClock = pygame.time.Clock()

	# initialize window
	DISPLAYSURF = pygame.display.set_mode((WINDOWSIZE,WINDOWSIZE),0,32)
	pygame.display.set_caption('Quantum Walk')

	while True:
		# clear layout for redraw
		DISPLAYSURF.fill(BLACK)

		# recalculate amplitudes at vertices
		U = qwalk(A, current_time)
		ampl = [U[i][0] for i in range(num_rows)]

		# recalculate probabilities at vertices (if measurement was taken now)
		prob = [(ampl[i] * ampl[i].conjugate()).real for i in range(num_rows)]

		# recalculate amplitudes to color-codes
		my_color = [int(prob[i] * 255) for i in range(num_rows)]

		# only use the red spectrum for now (to encode the amplitudes)
		Color = [(my_color[i],0,0) for i in range(num_rows)]

		# YOU ARE HERE

		# draw the edges
		for edge in G:
			pygame.draw.line(DISPLAYSURF, BLUE, Vertex[edge[0]], Vertex[edge[1]], thickness)

		# draw the vertices
		for i in range(len(Vertex)):
			# boundary
			pygame.draw.circle(DISPLAYSURF, RED, Vertex[i], 0+radius, radius)
			# fill
			pygame.draw.circle(DISPLAYSURF, Color[i], Vertex[i], radius, 0)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		# update time
		current_time += delta_time

		# update display
		pygame.display.update()

		# update clock
		fpsClock.tick(FPS)



############################################################################
# sample testing
# uncomment the lines below to run the program
# (change the first line accordingly)
############################################################################

# Step1: defining a graph
A = pathGraph(3)

# run the quantum walk simulation
qwalk_me(A)

############################################################################


