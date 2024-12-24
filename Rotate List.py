# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        count = 1
        curr = head
        while curr.next:
            curr = curr.next
            count += 1
        
        curr.next = head
        
        k = k % count 
    
        for _ in range(count - k):
            curr = curr.next
        
        new_head = curr.next
        curr.next = None
        
        return new_head
