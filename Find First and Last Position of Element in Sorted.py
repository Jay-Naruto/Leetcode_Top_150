class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findInLeft(nums,target):
            l=0
            r=len(nums)-1
            first=-1
            while l<=r:
                m=(l+r)//2
                if nums[m] == target:
                    first = m
                    r=m-1
                elif target > nums[m]:
                    l=m+1
                else:
                    r=m-1
            return first
        def findInRight(nums,target):
            l=0
            r=len(nums)-1
            last=-1
            while l<=r:
                m=(l+r)//2
                if nums[m] == target:
                    last = m
                    l=m+1
                elif target > nums[m]:
                    l=m+1
                else:
                    r=m-1
            return last
        f=findInLeft(nums,target)
        l=findInRight(nums,target)

        return [f,l]


        