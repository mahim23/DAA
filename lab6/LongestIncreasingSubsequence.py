arr = [5, 2, 8, 6, 3, 6, 9, 7]
n = len(arr)
dp = [None for _ in arr]
dp[0] = [0, -1]
for i in range(1, n):
    max = 0
    max_i = -1
    for k in range(i):
        if arr[k] < arr[i] and dp[k][0] + 1 > max:
            max = dp[k][0] + 1
            max_i = k
    dp[i] = [max, max_i]

m = [0, 0]
j = 0
for i in range(n):
    if dp[i][0] > m[0]:
        m = dp[i]
        j = i

sub_seq = [arr[j]]
while m[1] != -1:
    sub_seq.append(arr[m[1]])
    m = dp[m[1]]

print("Longest Increasing Subsequence:", sub_seq[::-1])