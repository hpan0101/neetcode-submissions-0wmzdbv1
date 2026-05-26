class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class LinkedList:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    
    def length(self):
        return self.size
    
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
        self.size += 1
    
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1
    
    def removeLeft(self) -> Node:
        if self.length() == 0:
            return None
        node = self.left.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodeMap = {}
        self.freqMap = defaultdict(LinkedList)
        self.minFreq = 0

    def counter(self, node: Node):
        cnt = node.freq
        self.freqMap[cnt].remove(node)
        if cnt == self.minFreq and self.freqMap[cnt].length() == 0:
            self.minFreq += 1
        node.freq += 1
        self.freqMap[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.nodeMap:
            node = self.nodeMap[key]

            node.val = value
            self.counter(node)
            return
        if len(self.nodeMap) == self.cap:
            node = self.freqMap[self.minFreq].removeLeft()
            del self.nodeMap[node.key]
        newNode = Node(key, value)
        self.nodeMap[key] = newNode
        self.minFreq = 1
        self.freqMap[1].insert(newNode)
# obj.put(key,value)