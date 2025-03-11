class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for w in word:
            if w not in d:
                d[w] = {}
            d=d[w]
        d['*'] = '*'

    def search(self, word: str) -> bool:
        return self.recursive(word, self.trie)
    
    def recursive(self,word, trie):
        d = trie
        for i, w in enumerate(word):
            if w == ".":
                for other in d:
                    if other != "*":
                        if self.recursive(word[i+1:] , d[other]):
                            return True
                return False
            elif w not in d:
                return False
            d=d[w]
        return '*' in d
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)