class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        sorted_str = sorted(str(binary),reverse=True)
        count=0
        for x in sorted_str:
            if x == '0':
                break
            count+=1
        return count


        