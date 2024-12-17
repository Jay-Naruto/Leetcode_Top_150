class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minimal=float('inf')
        l=0
        total=0
        for r in range(len(nums)):
            total+=nums[r]

            while total >= target:
                minimal = min(minimal, r-l + 1)
                total -= nums[l]
                l+=1
            
                
                
        
        return 0 if minimal == float('inf') else minimal