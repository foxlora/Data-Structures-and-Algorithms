'''
邻接表，有向图, 实现BFS,DFS
'''
from collections import defaultdict
class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def BFS(self,start):
        queue = []
        visited = [False] * len(self.graph)

        queue.append(start)
        visited[start] = True

        while queue:
            s = queue.pop()
            print(s,end=' ')
            for i in self.graph.get(s):
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True



    #不会写
    def DFS(self,start):

        visited = [False] * len(self.graph)
        self.DFSUtil(start,visited)


    def DFSUtil(self,v,visited):
        visited[v] = True
        print(v,end=" ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i,visited)






if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    #g.BFS(2)
    g.DFS(2)
