class BinaryMinHeap:

    def __init__(self, heap=None):
        if heap is None:
            heap = []
        self.heap = heap
        self.len = len(heap)
        if heap is not None:
            self.build_heap()


    @staticmethod
    def left(i):
        return i*2 + 1

    @staticmethod
    def right(i):
        return i*2 + 2

    @staticmethod
    def parent(i):
        if i == 0:
            return -1
        return (i-1) // 2

    def insert(self, k):
        self.heap.append(k)
        i = self.len
        self.len += 1
        while i > 0:
            p = BinaryMinHeap.parent(i)
            if self.heap[i] < self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def heapify(self, i):
        left = BinaryMinHeap.left(i)
        right = BinaryMinHeap.right(i)
        if left < self.len and self.heap[i] >= self.heap[left]:
            if right < self.len and self.heap[left] <= self.heap[right]:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            elif right < self.len:
                self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
                i = right
            else:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            self.heapify(i)
        elif right < self.len and self.heap[i] >= self.heap[right]:
            self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
            i = right
            self.heapify(i)

    def minimum(self):
        if self.len == 0:
            return None
        return self.heap[0]

    def extract_min(self):
        val = self.heap[0]
        self.len -= 1
        if self.len > 1:
            self.heap[0] = self.heap.pop(self.len)
            self.heapify(0)
        else:
            self.heap.pop(0)
        return val

    def build_heap(self):
        for i in range(BinaryMinHeap.parent(self.len - 1), -1, -1):
            self.heapify(i)

    def update_heap(self, i):
        while i > 0:
            p = BinaryMinHeap.parent(i)
            if self.heap[i] < self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def __str__(self):
        s = ""
        for i in self.heap:
            s += str(i) + " "
        return s