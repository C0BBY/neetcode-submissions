class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = {}
        for x in s1:
            store[x] = store.get(x, 0)+1

        for l in range((len(s2) - len(s1))+1):
            sub = s2[l:(l + len(s1))]
            dummy_map = {}
            for ch in sub:
                dummy_map[ch] = dummy_map.get(ch, 0)+1
            
            if dummy_map == store:
                print(dummy_map)
                print(store)
                return True

        return False

