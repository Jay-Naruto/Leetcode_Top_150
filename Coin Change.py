class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {}
        # def dp(amt):
        #     if amt == 0:
        #         return 0
        #     if amt in memo:
        #         return memo[amt] 
        #     minn = float('inf')
        #     for c in coins:
        #         if (amt - c) < 0:
        #             continue
        #         minn = min(minn, dp(amt - c)+1)
        #     memo[amt] = minn
        #     return minn
        
        # res = dp(amount)
        # return res if res != float('inf') else -1
        coins.sort()
        dp = [0]* (amount+1)
        for i in range(1,amount+1):
            minn = float('inf')
            for c in coins:
                diff = i-c
                if diff < 0:
                    break
                minn = min(minn, dp[diff]+1)
            dp[i] = minn
        
        return dp[-1] if dp[-1] != float('inf') else -1