class Solution:
    def fib(self, n: int) -> int:
        #top down
        # memo = {0:0, 1:1}

        # def f(x):
        #     if x not in memo:
        #         i = f(x-1)
        #         j = f(x-2)
        #         memo[x] = i + j
        #         return memo[x]
        #     else:
        #         return memo[x]
        
        # return f(n)

        #bottom up
        if n==0:
            return 0
        if n==1:
            return 1
        i,j = 0,1
        for x in range(2,n+1):
            i,j = j, i+j
        return j
        