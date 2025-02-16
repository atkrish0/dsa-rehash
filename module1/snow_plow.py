import networkx as nx

grid = nx.MultiGraph(nx.grid_2d_graph(2, 3))
grid = nx.eulerize(grid)
cycle = nx.eulerian_circuit(grid, source = (0, 0))

print(' -> '.join([str(edge[0]) for edge in cycle]))