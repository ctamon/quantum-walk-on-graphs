quantum-walk-on-graphs
======================

Visual Simulation of Quantum Walk on Graphs.

Comments:
- Implemented in python.
- Required libraries:
  1. numpy: for linear algebra (eigenvalues and eigenvectors).
  2. pygame: for graphical visualization (basic drawing routines).
  3. networkx, matplotlib.pyplot: for drawing graphs.

To run: on Linux, type the following on the command line:

  python qwalk.py
  
The output will be a simulation of a continuous-time quantum walk on a path on three vertices.

To try the program on another graph, change the line containing

  A = pathGraph(3)

