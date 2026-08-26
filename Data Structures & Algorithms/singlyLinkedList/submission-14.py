class ListNode:
    def __init__(self, val,next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(None)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        while curr:
            if index ==0:
                return curr.val
            index -=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val, self.head.next)
        self.head.next = new_head
        if not new_head.next:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head.next
        if index == 0:
            if curr:
                self.head.next = curr.next    
                if not curr.next:
                    self.tail = curr
                return True
            else:
                return False

        while curr.next: 
            if index == 1:
                curr.next = curr.next.next
                if not curr.next:
                    self.tail = curr
                return True
            index -=1
            curr = curr.next
        return False 


    def getValues(self) -> List[int]:
        retarr = []
        curr = self.head.next
        while curr:
            retarr.append(curr.val)
            curr = curr.next
        return retarr