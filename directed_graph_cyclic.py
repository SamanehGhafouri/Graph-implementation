"""Build Directed Cyclic Graph """

import networkx as nx
from matplotlib import pyplot as plt

graph = nx.DiGraph()
graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

print(nx.is_directed(graph))
print(nx.is_directed_acyclic_graph(graph))

"""Directed graphs that aren’t acyclic can’t be topologically sorted!!!!!!"""

"""Visualization"""
plt.tight_layout()
nx.draw_networkx(graph, arrows=True)
plt.savefig("Directed_acyc_graph.png", format="PNG")
plt.clf()
