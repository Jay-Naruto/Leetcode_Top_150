class Solution:
    def rob(self, nums: List[int]) -> int:
        #topdown
        # memo = {}
        # def dp(x):
        #     if x <0:
        #         return 0
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x] = max(dp(x-1), nums[x]+dp(x-2))
        #         return memo[x]

        # return dp(len(nums)-1)

        #bottomup
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
        return dp[-1]

        