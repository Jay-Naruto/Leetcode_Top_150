class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] = dict[nums[i]] + 1
            else:
                dict[nums[i]] = 1
        print(dict)
        for i in dict:
            if dict[i] > math.floor(len(nums) / 2):
                return i

        