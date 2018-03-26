from lab6.BinaryMinHeap import BinaryMinHeap


class Node:
    def __init__(self, symbol=None, freq=None, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
        self.code = None

    def __gt__(self, other):
        return self.freq > other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __ge__(self, other):
        return self.freq >= other.freq

    def __le__(self, other):
        return self.freq <= other.freq


class HuffmanCode:
    def __init__(self, symbols=None, freq=None):
        self.symbols = symbols
        self.freq = freq
        self.encoding = []
        if symbols:
            tree = self.build_tree()
            self.encode(tree, "")

    def build_tree(self):
        n = len(self.symbols)
        leaves = []
        for i in range(n):
            leaves.append(Node(self.symbols[i], self.freq[i]))
        self.encoding = leaves[:]

        heap = BinaryMinHeap(leaves)

        for i in range(n-1):
            x = heap.extract_min()
            y = heap.extract_min()
            tmp = Node(None, x.freq + y.freq, x, y)
            heap.insert(tmp)

        return heap.extract_min()

    def encode(self, tree, code):
        if tree.left is None and tree.right is None:
            tree.code = code
            return
        if tree.left is not None:
            self.encode(tree.left, code + "0")
        if tree.right is not None:
            self.encode(tree.right, code + "1")


if __name__ == '__main__':
    symbols = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [5, 9, 12, 13, 16, 45]
    huff_code = HuffmanCode(symbols, freq)
    size = 0
    print("Coding Scheme:")
    for i in huff_code.encoding:
        print(i.symbol, "=", i.code)
        size += i.freq*len(i.code)
    print("\nTotal size of file:", size)
