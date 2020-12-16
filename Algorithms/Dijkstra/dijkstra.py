from heapq import heappop, heappush
 
 
# Data structure to store graph edges
class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight
 
 
# Data structure to store heap nodes
class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
 
    # Override the __lt__() function to make `Node` class work with min heap
    def __lt__(self, other):
        return self.weight < other.weight
 
 
# class to represent a graph object
class Graph:
    def __init__(self, edges, N):
        # allocate memory for the adjacency list
        self.adj = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for edge in edges:
            self.adj[edge.source].append(edge)
 
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)
 
 
# Run Dijkstra's algorithm on given graph
def shortest_path(graph, source, N):
 
    # create min heap and push source node having distance 0
    pq = []
    heappush(pq, Node(source, 0))
 
    # set infinite distance from source to v initially
    dist = [float('inf')] * N
 
    # distance from source to itself is zero
    dist[source] = 0
 
    # list to track vertices for which minimum cost is already found
    done = [False] * N
    done[source] = True
 
    # stores predecessor of a vertex (to print path)
    prev = [-1] * N
    route = []
 
    # run till min heap is empty
    while pq:
 
        node = heappop(pq)          # Remove and return best vertex
        u = node.vertex             # get vertex number
 
        # do for each neighbor v of u
        for edge in graph.adj[u]:
            v = edge.dest
            weight = edge.weight
 
            # Relaxation step
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
 
        # marked vertex u as done so it will not get picked up again
        done[u] = True
 
    for i in range(1, N):
        if i != source and dist[i] != float('inf'):
            get_route(prev, i, route)
            print(f"Path ({source} -> {i}): Minimum Cost = {dist[i]}, Route = {route}")
            route.clear()
 
 
if __name__ == '__main__':
 
    # initialize edges as per above diagram
    # (u, v, w) triplet represent undirected edge from
    # vertex u to vertex v having weight w
    edges = [Edge(0, 1, 10), Edge(0, 4, 3), Edge(1, 2, 2),
             Edge(1, 4, 4), Edge(2, 3, 9), Edge(3, 2, 7),
             Edge(4, 1, 1), Edge(4, 2, 8), Edge(4, 3, 2)]
 
    # Set number of vertices in the graph
    N = 5
 
    # construct graph
    graph = Graph(edges, N)
 
    source = 0
    shortest_path(graph, source, N)

# Output:

# Path (0 -> 1): Minimum Cost = 4, Route = [0, 4, 1]
# Path (0 -> 2): Minimum Cost = 6, Route = [0, 4, 1, 2]
# Path (0 -> 3): Minimum Cost = 5, Route = [0, 4, 3]
# Path (0 -> 4): Minimum Cost = 3, Route = [0, 4]