
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mappings = {}
        heap_arr = []
        for i in nums:
            if i not in mappings:
                mappings[i] = 1
            else:
                mappings[i] +=1
        for i in mappings:
            heapq.heappush(heap_arr, (-mappings[i],i) )
        output= []
        for _ in range(k):
            _,y = heapq.heappop(heap_arr)
            output.append(y)
        return output
        
            