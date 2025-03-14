class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ''
        for w in strs:
            st += str(len(w)) + ',' + w 
        return st

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length_str = ''
            while s[i] != ",":
                length_str += s[i]
                i+=1
            i+=1
            res.append(s[i:i+int(length_str)])
            i+=int(length_str)
        return res





