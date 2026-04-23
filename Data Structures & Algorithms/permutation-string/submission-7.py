class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = {}
        for x in s1:
            store[x] = store.get(x, 0)+1

        for i in range(len(s2)):
            sub_map = {}
            for x in s2[i:i+len(s1)]:
                sub_map[x] = sub_map.get(x, 0)+1
            if sub_map == store:
                return True            

        return False                            