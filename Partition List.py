# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        part1=ListNode(0)
        currpart1=part1
        
        part2=ListNode(0)
        currpart2=part2
        curr=head
        while curr:
            if curr.val < x:
                currpart1.next = ListNode(curr.val)
                currpart1=currpart1.next
            curr=curr.next
            
        curr=head
        while curr:
            if curr.val >= x:
                currpart2.next = ListNode(curr.val)
                currpart2=currpart2.next
            curr=curr.next
            
            
        currpart1.next = part2.next
        
        return part1.next