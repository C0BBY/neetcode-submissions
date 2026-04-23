class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_cnt = 0
        for i, x in enumerate(heights):
            if not x:
                continue
            lowest = x
            max_cnt = max(max_cnt, x)

            for j in range(i + 1, len(heights)):
                lowest = min(lowest, heights[j])
                if not lowest:
                    break
                area = lowest * ((j-i) + 1)
                max_cnt = max(max_cnt, area)
        return max_cnt

