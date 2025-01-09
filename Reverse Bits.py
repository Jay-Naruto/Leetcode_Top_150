class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:].zfill(32)
        b=b[::-1]
        return int(b,2)
