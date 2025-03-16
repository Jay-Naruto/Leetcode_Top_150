# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        if l == 1:
            return None

        curr = head
        prev = None
        i = 0

        while curr:
            if i == (l - n):
                temp = curr.next
                if prev:
                    prev.next = temp  
                else:
                    return temp
                break
            else:
                prev = curr
                curr = curr.next
                i += 1

        return head

        