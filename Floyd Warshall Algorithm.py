#Floyd Warshall Algorithm
import timeit


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj = {} #Adjacency matrix that holds graph data
        self.vertexCount = 0

    def addVertex(self, vertex):
        if vertex in self.adj:
            return "Vertex already exists"
        if vertex != self.vertexCount:
            return "Don't skip a vertex"
        self.adj[vertex] = []
        self.vertexCount += 1

    def addEdge(self, start, end, weight):
        if start not in self.adj:
            return "Starting vertex not in graph"
        if end not in self.adj:
            return "Ending vertex not in graph"
        if start == end:
            return "Cannot have same start and end vertex"
        edge = Edge(start, end, weight)
        self.adj[start].append(edge)

    def doesEdgeExist(self, start, end):
        for vertex in self.adj:
            for edge in self.adj[vertex]:
                if edge.start == start and edge.end == end:
                    return (True, edge)
        return (False, None)

    def floydwarshall(self):
        M = [[9999999 for x in range(len(self.adj))] for y in range(len(self.adj))]
        for x in range(len(M)):
            for y in range(len(M[0])):
                if x == y:
                    M[x][y] = 0
                exists, edge = self.doesEdgeExist(x, y)
                if exists:
                    M[x][y] = edge.weight
        for k in range(len(M)):
            for i in range(len(M)):
                for j in range(len(M)):
                    newDistance = M[i][k] + M[k][j]
                    if newDistance < M[i][j]:
                        M[i][j] = newDistance
        return M


g = Graph()

g.addVertex(0)# 'A'
g.addVertex(1)# 'B'
g.addVertex(2)# 'C'
g.addVertex(3)# 'D'
g.addVertex(4)# 'E'
g.addVertex(5)# 'F'
g.addVertex(6)# 'G'
g.addVertex(7)# 'H'
g.addVertex(8)# 'I'

g.addEdge(0,1, 22)
g.addEdge(0,2, 9)
g.addEdge(0,3, 12)
g.addEdge(1, 2, 35)
g.addEdge(1, 5, 36)
g.addEdge(1, 7, 34)
g.addEdge(2, 5, 42)
g.addEdge(2, 4, 65)
g.addEdge(2, 3, 4)
g.addEdge(3, 4, 33)
g.addEdge(3, 8, 30)
g.addEdge(4, 5, 18)
g.addEdge(4, 6, 23)
g.addEdge(5, 7, 24)
g.addEdge(5, 6, 39)
g.addEdge(6, 7, 25)
g.addEdge(6, 8, 21)
g.addEdge(7, 8, 19)

print(g.floydwarshall())
print('The shortest path from Node "A" to Node "I" is 42')
print('Node A to self is 0')
print('Node A to Node B is 22')
print('Node A to Node C is 9...')

t = timeit.Timer("g.floydwarshall","from __main__ import g")
results = t.repeat(5, 10000)
for i,item in enumerate(results):
    print(i, '\t' , item)



