# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=head
        dict1={}
        while curr:
            if curr.val in dict1:
                dict1[curr.val] +=1
            else:
                dict1[curr.val] =1
            curr = curr.next
                
        curr1 = head
        newList = ListNode(0)
        curr2 = newList
        
        while curr1:
            if dict1[curr1.val] == 1:
                curr2.next = ListNode(curr1.val)
                curr2 = curr2.next
            curr1 = curr1.next
        
        return newList.next