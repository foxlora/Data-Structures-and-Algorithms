'''
(1) 初始时，S只包含起点s；U包含除s外的其他顶点，且U中顶点的距离为"起点s到该顶点的距离"[例如，U中顶点v的距离为(s,v)的长度，然后s和v不相邻，则v的距离为∞]。

(2) 从U中选出"距离最短的顶点k"，并将顶点k加入到S中；同时，从U中移除顶点k。

(3) 更新U中各个顶点到起点s的距离。之所以更新U中顶点的距离，是由于上一步中确定了k是求出最短路径的顶点，从而可以利用k来更新其它顶点的距离；例如，(s,v)的距离可能大于(s,k)+(k,v)的距离。

(4) 重复步骤(2)和(3)，直到遍历完所有顶点。
'''

from collections import defaultdict
from heapq import *

def dijkstra(edges,from_node ,to_node):
    graph = defaultdict(list)
    for l,r,c in edges:
        graph[l].append((c,r))

    q, seen = [(0,from_node,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1,path)
            if v1 == to_node:
                return cost,path
            for c, v2 in graph.get(v1,()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))
    return float("Inf")













if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]
    print(dijkstra(edges,'A','G'))








# # 迪克斯特拉算法： 计算加权图中的最短路径
# # graph: 起点start，a,b,终点fin之间的距离
# graph = {}
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["a"] = 2
# graph["a"] = {}
# graph["a"]["fin"] = 1
# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5
# graph["fin"] = {}
# # costs: 起点到 a,b,fin的开销
# infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity
# # parents： 存储父节点，记录最短路径
# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None
# # processed: 记录处理过的节点，避免重复处理
# processed = []
#
# #find_lowest_cost_node(costs): 返回开销最低的点
# def find_lowest_cost_node(costs):
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node
#
#
# #Dijkstra implement
# node = find_lowest_cost_node(costs)
# while node is not None:
#     cost = costs[node]
#     neighbors = graph[node]
#     for n in neighbors.keys():
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(costs)
#
# print(processed)