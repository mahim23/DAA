def majority(A):
    n = len(A)
    if n == 1:
        return A[0]
    l = majority(A[:n//2])
    r = majority(A[n//2:])
    lf = rf = 0
    for i in A:
        if i == l:
            lf += 1
        if i == r:
            rf += 1
    if lf > n/2:
        return l
    elif rf > n/2:
        return r
    return None

a = [1, 2, 4, 4, 5, 4, 4]
print("Majority element:", majority(a))