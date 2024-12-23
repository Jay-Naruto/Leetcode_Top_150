class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        output=[]
        k=0
        points.sort(key=lambda x : x[0])
        for i in range(1,len(points)):
            if points[i][0] > points[k][1]:
                output.append([points[k][0] , points[i-1][1]])
                k=i
                
            else:
                points[k][1] = min(points[k][1] , points[i][1])
        
        output.append([points[k][0] , points[k][1]])
        
        return len(output)