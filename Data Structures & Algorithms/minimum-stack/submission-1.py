class MinStack:

    def __init__(self):
        self.container = []
        self.min_item = []

    def push(self, val: int) -> None:        
        if self.min_item:
            self.min_item.append(
                min(val, self.min_item[-1])
            )
        else:
            self.min_item.append(val)                        
        self.container.append(val)
        


    def pop(self) -> None:
        self.container.pop()
        self.min_item.pop()        

    def top(self) -> int:
        return self.container[-1]
        
    def getMin(self) -> int:    
        return self.min_item[-1]