def merge(A1, A2):
    l = []
    inv = left = right = 0
    len1 = len(A1)
    len2 = len(A2)
    while left < len1 or right < len2:
        if left < len1 and right < len2 and A1[left] <= A2[right]:
            l.append(A1[left])
            left += 1
        elif left < len1 and right < len2:
            inv += len1 - left
            l.append(A2[right])
            right += 1
        elif left < len1:
            l.append(A1[left])
            left += 1
        else:
            l.append(A2[right])
            right += 1
    return l, inv

# naive method - O(n^2) time
#
# def inversions(A, beg, end):
#     if beg == end:
#         return 0
#     count = 0
#     for i in range(beg+1, end+1):
#         if A[beg] > A[i]:
#             count += 1
#     return count + inversions(A, beg+1, end)

def inversions(A):
    if len(A) == 1 or len(A) == 0:
        return A, 0
    A1, i1 = inversions(A[0:len(A)//2])
    A2, i2 = inversions(A[len(A)//2:])
    A3, i3 = merge(A1, A2)
    return A3, i1+i2+i3

s = input("Enter the array: ")
s = list(map(int, s.split()))
s, i = inversions(s)
print("\nNo. of inversions:", i)
print("Sorted Array:", s)
