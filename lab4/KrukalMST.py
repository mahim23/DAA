from lab4.DSU import *


def kruskal_mst(V, E):
    E.sort(key=weight)
    T = []
    ds = DSU()
    for i in V:
        ds.make_set(i)
    n = ds.nodes
    for u, v, w in E:
        if ds.find_set(n[u]) != ds.find_set(n[v]):
            T.append([u, v])
            ds.union(n[u], n[v])
    return T

def weight(l):
    return l[2]

n = 6
V = [x for x in range(n)]
E = [[0, 1, 3], [0, 3, 2], [0, 4, 2], [3, 4, 1], [1, 4, 1], [1, 2, 1], [1, 5, 3], [4, 2, 4], [4, 5, 2], [2, 5, 2]]
T = kruskal_mst(V, E)
print("Minimum Spanning Tree (edges):")
for i in T:
    print(i[0], i[1])
