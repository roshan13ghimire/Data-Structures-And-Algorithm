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
    
    def bfs(self,graph,source):
        visited = set()
        queue = deque()
        queue.append(source)
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex,end = " ")
                visited.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)

                
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
graph = g.print_graph()
g.bfs(graph,0)