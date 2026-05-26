class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    
    def length(self):
        return self.size
    
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        self.size += 1
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.size -= 1
    
    def removeLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.remove(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.nodeMap = {}
        self.freqMap = defaultdict(LinkedList)

    def counter(self, node):
        cnt = node.freq
        self.freqMap[cnt].remove(node)
        if cnt == self.min_freq and self.freqMap[cnt].length() == 0:
            self.min_freq += 1
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
            node = self.freqMap[self.min_freq].removeLeft()
            del self.nodeMap[node.key]

        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.freqMap[1].insert(node)
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)