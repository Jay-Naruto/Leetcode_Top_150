"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        dict1={}
        
        while curr:
            dict1[curr] = Node(curr.val)
            curr = curr.next
        curr =head
        while curr:
            if curr.next:
                dict1[curr].next = dict1[curr.next]
            if curr.random:
                dict1[curr].random = dict1[curr.random]
            curr = curr.next

            
        return dict1[head]
        