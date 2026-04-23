class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights)-1

        while left < right:
            base = right - left
            height = min(heights[right], heights[left])
            area = max(area,base*height)

            if heights[left] > height:
                right-=1
            else:
                left+=1                                

        return area
      