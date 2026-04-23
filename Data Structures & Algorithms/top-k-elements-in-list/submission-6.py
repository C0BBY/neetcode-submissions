class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        cont = []
        
        for x in nums:
            hm[x] = hm.get(x, 0)+1

        for x in hm.keys():
            cont.append((hm[x],x))

        cont.sort(reverse = True)
        return [x[-1] for x in cont][:k]

     