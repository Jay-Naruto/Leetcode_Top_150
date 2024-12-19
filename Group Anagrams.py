class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output={}
                    
        for i in range(len(strs)):
            x=sorted(strs[i])
            dump = "".join(x)
            if dump not in output:
                output[dump] = []
            output[dump].append(strs[i])
        
        return list(output.values())
            
                        
        