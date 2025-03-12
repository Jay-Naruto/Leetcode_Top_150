class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, sol =[], []
        def backtrack(num):
            if len(sol) == k:
                ans.append(sol[:])
                return
            left = n - num + 1  
            still_need = k - len(sol) 

            if left > still_need:
                backtrack(num + 1)

            sol.append(num)
            backtrack(num+1)
            sol.pop()

        backtrack(1)
        return ans
        