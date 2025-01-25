class Solution:
    def canJump(self, nums: List[int]) -> bool:

        k=0
        for i in range(len(nums)):
            if i > k:
                return False
            k = max(k, i + nums[i])
            if k >= len(nums)-1:
                return True
        return False


        
            

            
        
        
            
        