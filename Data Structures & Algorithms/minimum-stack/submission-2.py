class MinStack:

    def __init__(self):
        self.container = []

    def push(self, val: int) -> None:        
        min_item = val if not self.container else min(val,self.container[-1][1])    
        self.container.append((val, min_item))

    def pop(self) -> None:
        self.container.pop()

    def top(self) -> int:
        return self.container[-1][0]
        
    def getMin(self) -> int:    
        return self.container[-1][1]