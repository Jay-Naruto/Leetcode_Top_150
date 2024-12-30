# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        arr.sort()
        new_head=ListNode(0)
        curr=new_head
        i=0
        while curr and i < len(arr):
            node=ListNode(arr[i])
            curr.next=node
            i+=1
            curr=curr.next
        
        return new_head.next
        