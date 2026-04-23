class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        while nums:
            heapq.heappush(heap, nums.pop())
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]                