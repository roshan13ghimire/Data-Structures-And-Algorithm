class Graph:
    def __init__(self,num_vertices):
        self.V = num_vertices
        self.adj_matrix = [[0] * self.V for _ in range(self.V)]
    
    def add_edge(self,u,v):
        if u >= self.V or v >= self.V or u < 0 or v < 0:
            print("Invalid edge!")
        else:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
        
    def print_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
            
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_matrix()