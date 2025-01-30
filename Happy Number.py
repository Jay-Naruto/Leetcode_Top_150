class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumofsq(num):
            total=0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num = num // 10
            return total
        
        dict={}
        while n != 1:
            n = sumofsq(n)
            if n not in dict:
                dict[n] = True
            else:
                return False
            
        return True