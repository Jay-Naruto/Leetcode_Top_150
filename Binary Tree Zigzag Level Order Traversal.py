# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q=deque()
        q.append(root)
        arr=[]
        alternate = True
        while q:
            alternate = not alternate
            depth = len(q)
            dump=[]
            for _ in range(depth):
                node = q.popleft()
                dump.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            if alternate:
                dump.reverse()
            arr.append(dump)
        
        return arr
        