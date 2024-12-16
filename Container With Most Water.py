class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        ans=0
        
        while left < right:
            if (right-left) * min(height[right],height[left]) > ans:
                ans = (right-left) * min(height[right],height[left])
                
            if height[right] > height[left]:
                left+=1
            else:
                right-=1
        
        return ans