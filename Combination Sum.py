class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans, sol =[], []

        def backtrack(i, total):
            if total == target:
                ans.append(sol[:])
                return
            if total > target:
                return
            for x in range(i,n):
                sol.append(candidates[x])
                backtrack(x, total + candidates[x])
                sol.pop()
        backtrack(0,0)
        return ans
        