class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol =[], []

        def backtrack( open_b, close_b):
            if len(sol) == 2*n:
                ans.append("".join(sol[:]))
                return
            if open_b < n:
                sol.append("(")
                backtrack(open_b+1, close_b)
                sol.pop()
            if close_b < open_b:
                sol.append(")")
                backtrack(open_b, close_b+1)
                sol.pop()
            
        backtrack(0,0)
        return ans
            
            
        
        