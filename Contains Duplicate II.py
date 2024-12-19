class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1 = {}  
        for i in range(len(nums)):
            if nums[i] in dict1:
                if abs(i - dict1[nums[i]]) <= k:
                    return True  
            dict1[nums[i]] = i  
        
        return False  
