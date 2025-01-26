class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1] * len(nums)
        p=1
        for i in range(len(nums)):
            answer[i] = p
            p *= nums[i]
        s=1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * s
            s *= nums[i]
        
        return answer


                
        