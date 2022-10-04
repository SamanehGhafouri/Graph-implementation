"""
Building Directed Acyclic Graphs.
An acyclic graph is when a node can’t reach itself
"""

import networkx as nx

# for visualization
from matplotlib import pyplot as plt

graph = nx.DiGraph()
graph.add_edges_from([("root", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
nodes = graph.nodes()

shortest_path = nx.shortest_path(graph, "root", "e")
longest_path = nx.dag_longest_path(graph)
print(shortest_path)
print(longest_path)

"""Nodes in a DAG can be topologically sorted"""
topological_sort = list(nx.topological_sort(graph))
print(topological_sort)

"""Check to make sure the graph is directed"""
is_directed = nx.is_directed(graph)
print(is_directed)

is_directed_acyc_graph = nx.is_directed_acyclic_graph(graph)
print(is_directed_acyc_graph)

"""Visualization"""
plt.tight_layout()
nx.draw_networkx(graph, arrows=True)
plt.savefig("DAG.png", format="PNG")
plt.clf()


