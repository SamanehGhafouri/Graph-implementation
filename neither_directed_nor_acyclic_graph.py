"""Build a graph Neither Directed Nor Acyclic"""
import networkx as nx

graph = nx.Graph()
graph.add_edges_from([('x', 'y'), ('y', 'z')])

print(nx.is_directed(graph))
print(nx.is_directed_acyclic_graph(graph))
