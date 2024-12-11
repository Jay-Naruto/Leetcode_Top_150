class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        wordComplete=False
        for i in range(len(s)-1,-1,-1):
            if wordComplete == True:
                return count
            
            if s[i] == ' ' and count > 0:
                wordComplete = True
                # continue
            elif s[i] != ' ':
                count+=1
        return count
                
        