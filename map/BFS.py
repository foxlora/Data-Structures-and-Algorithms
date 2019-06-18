'''
邻接表，有向图, 实现BFS,DFS
'''
from collections import defaultdict,deque
class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def BFS(self,start):
        Q = deque()
        visited = [False] * len(self.graph)

        Q.append(start)
        visited[start] = True

        while Q:
            s = Q.popleft()
            print(s,end=' ')
            for i in self.graph.get(s):
                if not visited[i]:
                    Q.append(i)
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


def rec_dfs(G,s,S=None):
    if S is None:
        S = []
    S.append(s)
    for u in G.graph[s]:
        if u in S:
            continue
        rec_dfs(G,u,S)
    return S


def iter_dfs(G,s):
    S,Q=set(),[]
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G.graph[u])
        yield u


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.BFS(2)
    # g.DFS(2)
    # print(rec_dfs(g,2))
    # print(list(iter_dfs(g, 2)))
