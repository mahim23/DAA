men = [0, 1, 2, 3, 4]
women = men[:]
N = 5

mPref = [[1, 0, 3, 4, 2], [3, 1, 0, 2, 4], [1, 4, 2, 3, 0], [0, 3, 2, 1, 4], [1, 3, 0, 4, 2]]
wPref = [[4, 0, 1, 3, 2], [2, 1, 3, 0, 4], [1, 2, 3, 4, 0], [0, 4, 3, 2, 1], [3, 1, 4, 2, 0]]

mPref = [x[::-1] for x in mPref]

wPrefRev = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        wPrefRev[i][wPref[i][j]] = j

freeMen = men[:]

husband = [-1 for _ in range(N)]
wife = [-1 for _ in range(N)]

while len(freeMen) != 0:
    m = freeMen.pop()
    w = mPref[m].pop()
    if husband[w] == -1:
        husband[w] = m
        wife[m] = w
    elif wPrefRev[w][m] < wPrefRev[w][husband[w]]:
        m_ = husband[w]
        husband[w] = m
        wife[m] = w
        wife[m_] = None
        freeMen.append(m_)
    else:
        freeMen.append(m)

for i in range(N):
    print(chr(ord("V") + i), "-", chr(ord("A") + wife[i]))
