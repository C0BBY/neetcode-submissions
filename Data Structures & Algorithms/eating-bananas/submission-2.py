class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l<=r:
            mid = (l+r)//2
            hrs = 0
            for x in piles:
                hrs+= math.ceil(x/mid)
            if hrs > h:
                l = mid+1
            else:
                r = mid-1                                
        return l                
