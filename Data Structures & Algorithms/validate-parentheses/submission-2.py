class Solution:
    def isValid(self, s: str) -> bool:
        stk= []
        op = '([{'
        cl = ')]}'
        for i in s:
            if i in op:
                stk.append(i)
            else:
                try:
                    if cl.index(i)!=op.index(stk[-1]):
                        return False
                    stk.pop()
                except:
                    return False
        if len(stk)==0:
            return True
        else:
            return False