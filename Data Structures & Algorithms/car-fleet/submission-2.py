class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        upgrade = []
        stk = []

        for i in range(len(position)):
            upgrade.append((position[i], speed[i]))
        upgrade.sort()

        for i in range(len(upgrade)-1,-1, -1):
            pos = upgrade[i][0]
            spd = upgrade[i][-1]
            tim_taken = (target - pos) / spd            
            if not stk or tim_taken > stk[-1]:
                stk.append(tim_taken)

        return len(stk)