'''
判断无向图是否是一棵树
如果是一棵树，满足两个条件
1.无环
2.全连接
'''

from collections import defaultdict

class Graph(object):
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def iscycle(self,v,visited,parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if self.iscycle(i,visited,v) == True
                    return True

            elif i != parent:
                return True

        return False

    def istree(self):
        visited = [False] * self.V
        if self.iscycle(0,visited,-1) == True
            return False

        for i in range(self.V):
            if visited[i] == False:
                return False

        return True

