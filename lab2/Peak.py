def peak(A, beg, end):
    if end-beg <= 1:
        return max(A[beg: end+1])

    mid = (beg + end) // 2
    if A[mid-1] < A[mid] > A[mid+1]:
        return A[mid]
    elif A[mid-1] > A[mid]:
        return peak(A, beg, mid)
    else:
        return peak(A, mid+1, end)

s = input("Enter the array: ")
l = list(map(int, s.split()))
print("Peak:", peak(l, 0, len(l)-1))
