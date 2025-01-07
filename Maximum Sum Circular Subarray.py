class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            curr_s = max_s = nums[0]
            for x in nums[1:]:
                curr_s = max(x, curr_s + x)
                max_s = max(max_s, curr_s)
            return max_s

        max_kadane_og = kadane(nums)
        
        total = sum(nums)
        
        min_kadane_new_arr = kadane([-x for x in nums])
        max_circular = total + min_kadane_new_arr 

        if total == -min_kadane_new_arr:
            return max_kadane_og
        
        return max(max_kadane_og, max_circular)
        