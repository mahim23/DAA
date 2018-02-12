men = [0, 1, 2, 3, 4]
women = men[:]

mPref = [[1, 0, 3, 4, 2], [3, 1, 0, 2, 4], [1, 4, 2, 3, 0], [0, 3, 2, 1, 4], [1, 3, 0, 4, 2]]
wPref = [[4, 0, 1, 3, 2], [2, 1, 3, 0, 4], [1, 2, 3, 4, 0], [0, 4, 3, 2, 1], [3, 1, 4, 2, 0]]

mPrefRev = [[0 for _ in range(5)] for _ in range(5)]
wPrefRev = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        wPrefRev[i][wPref[i][j]] = j
        mPrefRev[i][mPref[i][j]] = j

def isStable(w):
    h = [-1 for _ in range(5)]
    for i in range(5):
        h[w[i]] = i

    for i in range(5):
        for j in range(wPrefRev[w[i]][i]):
            k = wPref[w[i]][j]
            if mPrefRev[k][w[i]] < mPrefRev[k][w[k]]:
                return False
        for j in range(mPrefRev[h[i]][i]):
            k = mPref[h[i]][j]
            if wPrefRev[k][h[i]] < wPrefRev[k][h[k]]:
                return False
    return True

wife = [x for x in range(5)]

def permute(a, l, r):
    if l == r:
        if isStable(a):
            print(a)
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

permute(wife, 0, 4)