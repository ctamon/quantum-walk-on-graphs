#####################################################################################
# qtools.py
# HELPERS FOR SPECTRAL DECOMPOSITION AND QUANTUM WALK SIMULATION
#####################################################################################

import sys, math, numpy

#####################################################################################
# quantum walk on a graph G (defined by a matrix A) at time t
# using: exp(-jtA)
#####################################################################################
def qwalk(A,t):
	B = specdecomp(A)
	eigenvalues = B[0]
	eigenprojectors = B[1]
	
	[num_rows, num_cols] = A.shape
	U = (numpy.zeros(shape = (num_rows, num_cols))).astype(complex)

	for j in range(len(eigenvalues)):
		U += (numpy.exp(-1j * complex(t * eigenvalues[j])) * eigenprojectors[j].astype(complex))

	return U


#####################################################################################
# specdecomp: 
#  computes the spectral decomposition of a matrix A
# input: matrix A
# output: a list of eigenvalues of A and a list of its corresponding eigenprojectors
#####################################################################################
def specdecomp(A):
	[eigenvalue_list, row_eigenmatrix] = numpy.linalg.eigh(A)
	[num_rows, num_cols] = A.shape

	eigenmatrix = numpy.asmatrix(row_eigenmatrix)
	eigenmatrix = eigenmatrix.H
	
	eigenvalues = []
	eigenprojectors = []
	for i in range(num_rows):
		found = False
		for j in range(len(eigenvalues)):
			if abs(eigenvalue_list[i] - eigenvalues[j]) < 0.0001:
				v = eigenmatrix[i].H
				eigenprojectors[j] += (v * v.H)
				found = True

		if found == False:
			eigenvalues.append(eigenvalue_list[i])
			v = eigenmatrix[i].H
			eigenprojectors.append(v * v.H)

	return [eigenvalues, eigenprojectors]


#####################################################################################
# verifier: checks if the eigenprojectors of a matrix A sum to identity
#####################################################################################
def testBasis(A, eigenprojectors):
	[num_rows, num_cols] = A.shape
	Z = numpy.zeros(shape = (num_rows, num_cols))

	for j in range(len(eigenprojectors)):
		Z += eigenprojectors[j]

	Identity = numpy.identity(num_rows)

	# return the matrix 2-norm of Z - Identity
	return numpy.linalg.norm((Z-Identity).astype(float), 2)


#####################################################################################
# verifier: checks if A = Sum_{i} Eigenvalue[i]*EigenProjector[i]
#####################################################################################
def testDecomp(A, eigenvalues, eigenprojectors):
	[num_rows, num_cols] = A.shape
	Z = numpy.zeros(shape = (num_rows, num_cols))

	if len(eigenvalues) != len(eigenprojectors):
		return Z
	for j in range(len(eigenvalues)):
		Z += (complex(eigenvalues[j]) * eigenprojectors[j])

	# return the matrix 2-norm of Z - A
	return numpy.linalg.norm((Z-A).astype(float), 2)



#####################################################################################
# LOCAL TESTING
#####################################################################################
def testMe(n, show=False):
	A = skewClique(n)
	if show == True:
		print "A = ", A

	B = specdecomp(A)
	if show == True:
		print "EigenValues = ", B[0]
		print "EigenVectors = ", B[1]

	print "||I - SUM Eigenprojectors|| <= ", testBasis(A, B[1])
	print "||A - SUM Eigenvalue * Eigenprojector|| <= ", testDecomp(A, B[0], B[1])
	U = qwalk(A, 0)
	#print "||U - U.H|| <= ", numpy.linalg.norm((U - U.T).astype(float), 2)
	#print "exp(-itA) = "
	#print U
	return numpy.asmatrix(U)
#####################################################################################


