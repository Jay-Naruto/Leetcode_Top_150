class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arrs=[''] * numRows
        check='down'
        index=0
        
        for i in range(len(s)):
            if index <= numRows -1:
                if check == 'down':
                    arrs[index] +=s[i]
                    if index == numRows-1:
                        check = 'up'
                        index -= 1
                    elif index < numRows-1:
                        index +=1
                        check = 'down'
                elif check == 'up':
                    arrs[index] +=s[i]
                    if index == 0:
                        index+=1
                        check = 'down'
                    elif index > 0:
                        index -= 1
                        check = 'up'
        
        ans=''
        
        for strings in arrs:
            ans+=strings
        
        return ans
                

