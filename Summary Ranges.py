class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        output=[]
        k=0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                if i-1 == k:
                    output.append(str(nums[k]))
                else:
                    output.append(str(nums[k]) +"->"+ str(nums[i-1]))
                
                k=i
        if k == len(nums)-1:
            output.append(str(nums[k]))
        else:
            output.append(str(nums[k]) +"->"+ str(nums[-1]))
                
        return output