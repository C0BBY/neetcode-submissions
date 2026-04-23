class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                base = j - i
                height = min(heights[i], heights[j])            
                vol = max(vol, base*height)
        return vol