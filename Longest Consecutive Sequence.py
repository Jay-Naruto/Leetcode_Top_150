class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numset=set(nums)
        
        longest=0
        
        for num in numset:
            if num-1 not in numset:
                curr_num=num
                curr_l=1
                
                while curr_num + 1 in numset:
                    curr_l +=1
                    curr_num += 1
                longest=max(longest, curr_l)
        return longest