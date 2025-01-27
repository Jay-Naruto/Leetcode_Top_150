class Solution:
    def reverseWords(self, s: str) -> str:
        arr=[]
        word=''
        ans=''
        for i in range(len(s)):
            if s[i] != " ":
                word += s[i]
            else:
                if len(word) > 0:
                    arr.append(word)
                    word=''
        if word: arr.append(word)
        for i in range(len(arr)-1,-1,-1):
            ans += arr[i]
            if i != 0:
                ans += " "
        return ans
                
