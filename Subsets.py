class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol =[], []

        def backtrack(i):
            if i == n:
                ans.append(sol[:])
                return
            #1st way, don't pick the number
            backtrack(i+1)

            #2nd way, pick it
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return ans