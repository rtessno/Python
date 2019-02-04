#Dijkstra's Algorithm
import collections
import math
import timeit


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex: pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    S = set()
    delta = dict.fromkeys(list(graph.vertices), math.inf)
    previous = dict.fromkeys(list(graph.vertices), None)
    delta[start] = 0
    while S != graph.vertices:
        v = min((set(delta.keys()) - S), key=delta.get)
        for neighbor in set(graph.edges[v]) - S:
            new_path = delta[v] + graph.weights[v, neighbor]
            if new_path < delta[neighbor]:
                delta[neighbor] = new_path
                previous[neighbor] = v
        S.add(v)
    return (delta, previous)


def shortest_path(graph, start, end):
    delta, previous = dijkstra(graph, start)
    path = []
    vertex = end
    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]
    path.reverse()
    return path

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')
g.add_vertex('H')
g.add_vertex('I')

g.add_edge('A', 'B', 22)
g.add_edge('A', 'C', 9)
g.add_edge('A', 'D', 12)
g.add_edge('B', 'C', 35)
g.add_edge('B', 'F', 36)
g.add_edge('B', 'H', 34)
g.add_edge('C', 'F', 42)
g.add_edge('C', 'E', 65)
g.add_edge('C', 'D', 4)
g.add_edge('D', 'E', 33)
g.add_edge('D', 'I', 30)
g.add_edge('E', 'F', 18)
g.add_edge('E', 'G', 23)
g.add_edge('F', 'H', 24)
g.add_edge('F', 'G', 39)
g.add_edge('G', 'H', 25)
g.add_edge('G', 'I', 21)
g.add_edge('H', 'I', 19)

# print(g)
# print('###')
print(shortest_path(g,'A','I'))

t = timeit.Timer("shortest_path(g,'A','I')","from __main__ import shortest_path, g")
results = t.repeat(5, 10000)
for i,item in enumerate(results):
    print(i, '\t' , item)
