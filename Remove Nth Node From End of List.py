# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        count = 0
        curr = head
        while curr:
            count+=1
            curr=curr.next
            
        if count == n:
            return head.next
        
        curr=head
        
        for _ in range(count - n - 1):
            curr = curr.next
            
        if curr.next:
            temp = curr.next.next
            curr.next.next = None
            curr.next = temp
        else:
            curr.next.next = None
        
        return head