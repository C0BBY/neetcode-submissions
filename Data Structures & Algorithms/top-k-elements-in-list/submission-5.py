class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(f"{nums}  {k}")
        
        count = {}
        tuplist = []
        for i in nums:
            count[i] = count.get(i, 0)+1                 

        for c in count.keys():
            tuplist.append((count[c], c))
        return [x[-1] for x in sorted(tuplist, reverse = True)[:k]]