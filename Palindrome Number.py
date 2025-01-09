class Solution:
    def isPalindrome(self, x: int) -> bool:
        if len(str(x)) == 1:
            return True
        l=0
        r=len(str(x))-1

        while l <= r:
            if str(x)[l] != str(x)[r]:
                return False
            l=l+1
            r=r-1
        return True
        