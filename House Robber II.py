class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n==1:
            return nums[0]
        def dp(arr, memo, i):
            if i < 0:
                return 0
            if i not in memo:
                memo[i] = max(dp(arr, memo, i-1), arr[i] + dp(arr, memo, i-2))
                return memo[i]
            else:
                return memo[i]

        return max(dp(nums[1:], {}, len(nums)-2), dp(nums[:-1], {}, len(nums)-2))
        # n = len(nums)
        # if n==1:
        #     return nums[0]
        # def rec(arr):
        #     if len(arr) == 0:
        #         return 0
        #     if len(arr) == 1:
        #         return arr[0]
        #     dp = [0] * len(arr)
        #     dp[0] = arr[0]
        #     for i in range(1, len(arr)):
        #         dp[i] = max(dp[i-1], arr[i]+dp[i-2])
        #     return dp[-1]
        
        # return max(rec(nums[1:]), rec(nums[:-1]))
        