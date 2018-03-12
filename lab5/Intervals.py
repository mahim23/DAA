def end_time(a):
    return a[1]

def max_jobs(intervals, n):
    l = []
    intervals.sort(key=end_time)
    prev = 0
    for interval in intervals:
        if interval[0] >= prev:
            l.append(interval)
            prev = interval[1]
    return l


if __name__ == '__main__':
    n = 8
    intervals = [[1, 3], [2, 8], [2, 5], [3, 7], [4, 8], [4, 6], [6, 12], [7, 10]]
    max_j = max_jobs(intervals, n)
    print("Maximum no. of non-overlapping intervals: {}\nIntervals: {}".format(len(max_j), max_j))
