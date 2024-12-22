class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output=[]
        k=0
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        
        for i in range(1,len(intervals)):
            if intervals[i][0] > intervals[k][1]:
                output.append([intervals[k][0] , intervals[k][1]])
                k=i
            else:
                intervals[k][1] = max(intervals[k][1] , intervals[i][1])
        output.append([intervals[k][0] , intervals[k][1]])  
        return output