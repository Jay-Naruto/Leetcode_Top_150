class Solution:
    def climbStairs(self, n: int) -> int:
        #bottomup
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # dp = [0]*(n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for x in range(3,n+1):
        #     dp[x] = dp[x-1] + dp[x-2]
        # return dp[n]

        #topdown
        memo = {1:1, 2:2}

        def steps(x):
            if x not in memo:
                memo[x] = steps(x-1) + steps(x-2)
                return memo[x]
            else:
                return memo[x]

        return steps(n)
