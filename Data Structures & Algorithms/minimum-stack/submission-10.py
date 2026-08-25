class MinStack:

    def __init__(self):
       self.stk = []
       
       self.minvalues = {}
       self.currentmin = None
    
    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.currentmin == None or val<self.currentmin:
            self.minvalues[len(self.stk)] = val
            self.currentmin = val            


    def pop(self) -> None:
        l = len(self.stk)
        if l in self.minvalues.keys():
            del self.minvalues[l]
            if self.minvalues != {}:
                self.currentmin = self.minvalues[max(self.minvalues.keys())] 
            else:
                self.currentmin=None
        self.stk.pop()
    
    def top(self) -> int:
       return self.stk[-1] 

    def getMin(self) -> int:
        return self.currentmin
