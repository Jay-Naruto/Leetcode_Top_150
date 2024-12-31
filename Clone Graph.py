"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new_node = Node(node.val)
        dict1={}
        dict1[node] = new_node
        check=[node]
        while check:
            curr_node=check.pop()
            for x in curr_node.neighbors:
                if x not in dict1:
                    dict1[x] = Node(x.val)
                    check.append(x)
                dict1[curr_node].neighbors.append(dict1[x])
                
        return dict1[node]