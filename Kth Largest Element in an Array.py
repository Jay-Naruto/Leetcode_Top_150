class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        x=0
        for _ in range(len(nums) - k+1):
            x=heapq.heappop(nums)
        return x
        