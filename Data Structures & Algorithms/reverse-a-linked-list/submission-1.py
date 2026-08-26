# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr or not  curr.next:
            return curr
        next_node = curr.next
        while next_node:
            prev = curr
            curr = next_node
            next_node = curr.next
            curr.next = prev
        head.next = None
        return curr