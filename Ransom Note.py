class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dump = magazine
        for char in ransomNote:
            if char in dump:
                dump=dump.replace(char,"",1)
            else:
                return False
        return True
        
            
        