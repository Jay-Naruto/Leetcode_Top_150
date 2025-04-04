class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_d = -1
        start = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[start]:
                start = i
            else:
                max_d = max(max_d, nums[i] - nums[start])
        return max_d