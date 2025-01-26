
import random
class RandomizedSet:

    def __init__(self):
        self.map={}
        self.array=[]
        
    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.array.append(val)
            self.map[val] = len(self.array)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            index = self.map[val]
            self.array[index] = self.array[-1]
            self.map[self.array[-1]] = index
            self.array.pop()
            del self.map[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()