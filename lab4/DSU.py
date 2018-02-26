class Node:
    def __init__(self, index=None, rank=None, rep=None):
        self.index = index
        self.rank = rank
        self.rep = rep

class DSU:
    def __init__(self):
        self.nodes = []

    def make_set(self, x):
        tmp = Node(x, 0)
        tmp.rep = tmp
        self.nodes.append(tmp)

    def find_set(self, x):
        tmp = x
        while tmp.rep is not tmp:
            tmp = tmp.rep
        x.rep = tmp
        return tmp

    def union(self, x, y):
        x = self.find_set(x)
        y = self.find_set(y)
        if x.rank > y.rank:
            y.rep = x
        elif x.rank < y.rank:
            x.rep = y
        else:
            x.rep = y
            y.rank += 1

    def print_sets(self):
        l = [[] for _ in self.nodes]
        for i, x in enumerate(self.nodes):
            rep = self.find_set(x)
            l[rep.index].append(i)
        print("Sets are:")
        for i in l:
            if i:
                for j in i:
                    print(j, end=" ")
                print()

if __name__ == "__main__":
    ds = DSU()
    for i in range(7):
        ds.make_set(i)
    n = ds.nodes
    ds.union(n[0], n[1])
    ds.print_sets()
    ds.union(n[0], n[2])
    ds.print_sets()
    ds.union(n[2], n[3])
    ds.print_sets()
    ds.union(n[4], n[6])
    ds.print_sets()
    ds.union(n[4], n[5])
    ds.print_sets()
    ds.union(n[2], n[4])
    ds.print_sets()
