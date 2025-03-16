# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mappings_to_prev = {}
        tail = head
        mappings_to_prev[tail] = None
        while tail.next:
            prev = tail
            tail = tail.next
            mappings_to_prev[tail] = prev
        curr=head
        while curr != tail and curr.next != tail:
            temp = curr.next
            curr.next = tail
            tail.next = temp
            curr = temp
            tail = mappings_to_prev[tail]
        tail.next = None

        