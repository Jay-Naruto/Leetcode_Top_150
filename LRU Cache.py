class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache={}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self,node:ListNode):
        prev = node.prev
        nextNode=node.next
        prev.next = nextNode
        nextNode.prev = prev
        
    def add_to_tail(self,node:ListNode):
        prev = self.tail.prev
        prev.next = node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add_to_tail(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add_to_tail(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
                
            newNode = ListNode(key,value)
            self.cache[key] = newNode
            self.add_to_tail(newNode)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)