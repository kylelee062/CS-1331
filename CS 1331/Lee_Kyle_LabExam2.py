class UndirectedGraph:
    def __init__(self, n):
        self.n = n 
        self.adj = [[0] * n for i in range(n)] 

    def add_edge(self, u, v):
        self.adj[u][v] = 1
        self.adj[v][u] = 1

    def node_exists(self, u):
        return 0 <= u < self.n

    def edge_exists(self, u, v):
        if not self.node_exists(u) or not self.node_exists(v):
            return False
        return self.adj[u][v] == 1
    
    def get_neighbors(self, u):
        if not self.node_exists(u):
            return []
        neighbor_list = []
        for v in range(self.n):
            if self.adj[u][v] == 1:
                neighbor_list.append(v)
        return neighbor_list
    
    def get_edge_density(self):
        possible = (self.n * (self.n - 1)) // 2
        actual = sum(sum(row) for row in self.adj) // 2
        total = actual / possible if possible > 0 else 0
        return total

    def is_complete(self):
        return self.get_edge_density() == 1.0
    
graph = UndirectedGraph(4) # creates graph with 4 nodes
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,3)

print(graph.node_exists(1)) # expected output: True
print(graph.node_exists(10)) # expected output: False

print(graph.edge_exists(1,2)) # expected output: True
print(graph.edge_exists(1,3)) # expected output: False

print(graph.get_neighbors(1)) # expected output: [0,2]

print(graph.get_edge_density()) # expected output: 0.67

print(graph.is_complete()) # expected output: False

