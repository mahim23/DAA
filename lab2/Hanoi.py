def solveHanoi(n, s, i, t):
    if n == 1:
        print("Move disc 1 from", s, "to", t)
        return
    solveHanoi(n-1, s, t, i)
    print("Move disc", n, "from", s, "to", t)
    solveHanoi(n-1, i, s, t)

n = input("Enter the no. of disks: ")
solveHanoi(int(n), "S", "I", "T")
