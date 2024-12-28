# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque()
        q.append(root)
        arr=[]

        while q:
            rightNode = q[0]
            arr.append(rightNode.val)
            for _ in range(len(q)):
                node=q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        
        return arr

        