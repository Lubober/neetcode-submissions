# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(None)
        point1 = list1
        point2 = list2
        
        current = new_head

        while point1 and point2:
            if point1.val > point2.val:
                current.next = point2
                point2 = point2.next
            else:
                current.next = point1
                point1 = point1.next
            current = current.next
        
        if point1:
            current.next = point1
        
        if point2:
            current.next = point2
        return new_head.next