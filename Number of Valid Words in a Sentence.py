class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        counter = 0
        for w in words:
            flag = True
            #case1
            for i in w:
                if i.isdigit():
                    flag = False
                    break
            if not flag:
                continue
            
            #case2
            if w.count('-') > 1:
                continue

            if '-' in w:
                idx = w.index('-')
                if idx == 0 or idx == len(w)-1:
                    continue
                if not (w[idx - 1].islower() and w[idx + 1].islower()):
                    continue

            #case3
            puncs = ['!',',','.']
            puncs_count = sum(w.count(p) for p in puncs)
            if puncs_count > 1:
                continue
            if puncs_count == 1 and w[-1] not in puncs:
                continue
            if puncs_count == 1:
                for j in range(len(w)-1):
                    if w[j] in puncs:
                        flag = False
                        break
                if not flag:
                    continue
            if flag:
                counter +=1
        return counter
                    
        