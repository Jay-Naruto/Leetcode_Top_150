"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        q=deque()
        q.append(root)
        
        while q:
            level = len(q)
            prev=None
            
            for _ in range(level):
                node = q.popleft()
                
                if prev:
                    prev.next = node
                prev = node
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if prev:
                prev.next = None
        
        return root
        