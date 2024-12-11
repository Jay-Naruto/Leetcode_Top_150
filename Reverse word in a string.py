class Solution:
    def reverseWords(self, s: str) -> str:
        answer=[]
        flag = False
        dump=''
        for i in range(len(s)):
            if s[i] != ' ':
                dump+=s[i]
                flag = True
            elif s[i] == ' ' and flag == True:
                answer.append(dump)
                dump=''
                flag = False
                
        if dump != '':
            answer.append(dump)
            
        
        answer.reverse()
        dump=''
        for i in range(len(answer)):
            
            dump+=answer[i]
            dump+=' '
            
        
        return dump[:-1]
            
        