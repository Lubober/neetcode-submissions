class LinkedList:
    
    def __init__(self):
       self.head = None
       self.tail = None 
    
    def get(self, index: int) -> int:
        iter_list = self.head
        if not self.head:
            return -1
        while index > 0:
            iter_list = iter_list.nxt
            if not iter_list:
                return -1

            index -= 1
        return iter_list.val
        


    def insertHead(self, val: int) -> None:
       self.head = ListNode(val, self.head) 
       if self.head.nxt == None:
           self.tail=self.head

    def insertTail(self, val: int) -> None:
        if self.tail:
            self.tail.nxt = ListNode(val,None)
            self.tail = self.tail.nxt
        else:
            self.tail = self.head = ListNode(val,None)

    def remove(self, index: int) -> bool:
        iter_list = self.head
        if not iter_list:
            return False
        if not iter_list.nxt:
            if index>0:
                return False
            self.head = self.tail = None 
            return True
        if index == 0:
            self.head = self.head.nxt
            return True
        while index>1:
            iter_list = iter_list.nxt
            if not iter_list.nxt:
                return False
            index -= 1
        
        iter_list.nxt = iter_list.nxt.nxt
        if not iter_list.nxt:
            self.tail = iter_list
        self.getValues()
        return True


    def getValues(self) -> List[int]:
        ret_arr = []
        iter_list = self.head
        while iter_list:
            ret_arr.append(iter_list.val)
            iter_list = iter_list.nxt
        return ret_arr

        
class ListNode:

    def __init__(self,val,nxt):
        self.val = val
        self.nxt = nxt