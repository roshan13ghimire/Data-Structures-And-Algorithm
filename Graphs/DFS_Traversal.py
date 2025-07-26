from collections import deque

class Graph:
    def __init__(self,num_vertices):
        self.V = num_vertices
        self.adj_list = {i: [] for i in range(self.V)}
    
    def add_edge(self,u,v):
        if u >= self.V or v >= self.V or u < 0 or v < 0:
            print("Invalid edge!")
        else:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        
    def print_graph(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
        return self.adj_list
    
                    
    
    def dfs(self,graph,source,visited = None):
        if visited is None:
            visited = set()
        visited.add(source)
        print(source,end = " ")
        for neighbour in graph[source]:
            if neighbour not in visited:
                visited.add(neighbour)
                self.dfs(graph,neighbour,visited)
            

                
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
graph = g.print_graph()
g.dfs(graph,0)