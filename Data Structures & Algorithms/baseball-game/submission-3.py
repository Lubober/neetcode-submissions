import numpy as np
class Solution:
    def __init__(self):
        self.scores=[0]

    def calPoints(self, operations: List[str]) -> int:
        for i in operations:
            self.operate( i)
        return int(np.array(self.scores).sum())

    def operate(self, operation):
        try:
            self.scores.append(int(operation))
        except:
            match operation:
                case '+':
                    self.scores.append(self.scores[-1]+self.scores[-2])
                case 'D':
                    self.scores.append(self.scores[-1]*2)
                case 'C':
                    self.scores.pop()
        