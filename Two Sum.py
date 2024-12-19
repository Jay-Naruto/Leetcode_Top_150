class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [i, dict[target - nums[i]]]
            
            dict[nums[i]] = i
            
