"""Build Directed Acyclic Graph that has multiple root nodes."""

import networkx as nx

graph = nx.DiGraph()
graph.add_edges_from([('m', 'p'), ('n', 'p'), ('o', 'p'), ('p', 'q')])

print(nx.is_directed(graph))
print(nx.is_directed_acyclic_graph(graph))

"""A directed graph can have multiple valid topological sorts.
m, n, o, p, q is another way to topologically sort this graph."""
print(list(nx.topological_sort(graph)))
