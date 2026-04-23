class MinStack:

    def __init__(self):
        self.container = []
        self.hmap = {}
        self.min_item = 0

    def push(self, val: int) -> None:        
        self.container.append(val)
        print(f"push {self.container}")
        # self.hmap[val] = self.hmap.get(val, 0)+1
        

    def pop(self) -> None:
        self.container.pop()
        print(f"pop {self.container}")
        # self.hmap[val] = self.hmap.get(val, 0)+1    
        # if not self.hmap[val]:
        #     self.hmap.remove(val)

        

    def top(self) -> int:
        return self.container[-1]
        

    def getMin(self) -> int:
        holder = self.container[:]
        holder.sort()
        return holder[0]