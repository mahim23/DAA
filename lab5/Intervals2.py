def min_resources(intervals, n):
    res = []
    intervals.sort(key=lambda a: a[0])
    intervals.sort(key=lambda a: a[1])
    c = 0
    while True:
        l = []
        prev = 0
        for i, interval in enumerate(intervals):
            if interval is not None and interval[0] >= prev:
                l.append(interval)
                prev = interval[1]
                c += 1
                intervals[i] = None
        res.append(l)
        if c == n:
            break
    return res


if __name__ == '__main__':
    # n = 10
    # intervals = [[1, 3], [1, 6], [1, 3], [4, 6], [4, 10], [8, 12], [8, 12], [11, 15], [13, 15], [13, 15]]
    n = 4
    intervals = [[1, 5], [7, 10], [1, 7], [6, 10]]
    min_res = min_resources(intervals, n)
    print("Minimum no. of resources: {}".format(len(min_res)))
    for i, res in enumerate(min_res):
        print("Resource {} jobs: {}".format(i+1, res))
