# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=None
        rem=0
        current1 = l1
        current2 = l2
        l3 = ListNode(0)
        curr = l3
        while current1 or current2:
            if not current1 :
                x = ListNode(0)
                current1 = x
            elif not current2:
                x = ListNode(0)
                current2 = x
                
            if current1.val + current2.val > 9:
                if carry:
                    x = current1.val + current2.val + carry
                    carry = (x) // 10
                    rem = (x) % 10
                    curr.next = ListNode(rem)
                else:
                    carry = (current1.val + current2.val) // 10
                    rem = (current1.val + current2.val) % 10
                    curr.next = ListNode(rem)
            else:
                if carry:
                    x = current1.val + current2.val + carry
                    carry = (x) // 10
                    rem = (x) % 10
                    curr.next = ListNode(rem)
                else:
                    x = current1.val + current2.val
                    curr.next = ListNode(x)
                    carry = None
            
            current1 = current1.next            
            current2 = current2.next
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)
        return l3.next