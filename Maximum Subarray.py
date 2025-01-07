class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s=float('-inf')
        curr_s=0

        for i in range(len(nums)):
            curr_s += nums[i]
            max_s = max(max_s , curr_s)

            if curr_s < 0:
                curr_s=0
        
        return max_s