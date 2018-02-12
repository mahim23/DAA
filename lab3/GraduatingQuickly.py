def minSem(AL, n):
    l = [0 for _ in range(n)]
    q = []
    k = n
    sem = 0
    for i in range(n):
        sem = 1
        for j in AL[i]:
            l[j] += 1
    for i in range(n):
        if l[i] == 0:
            q.append(i)
            k -= 1
    while k > 0:
        sem += 1
        p = []
        for i in q:
            for j in AL[i]:
                l[j] -= 1
                if l[j] == 0:
                    p.append(j)
                    k -= 1
        q = p
    return sem

AL = [[1], [2, 5], [3], [], [5], [6], []]
n = len(AL)
print("Adjacency List:")
for i in range(n):
    print("Vertex", str(i) + ": ", end="")
    for j in AL[i]:
        print(j, end=" ")
    print()
print("\nMinimum no. of semesters required:", minSem(AL, n))
