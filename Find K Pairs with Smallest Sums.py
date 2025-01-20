class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        H=[]
        ans=[]
        for i in range(min(k, len(nums1))):
            heappush(H, (nums1[i] + nums2[0], i, 0))
        
        while H and len(ans) < k:
            _,i,j = heapq.heappop(H)
            ans.append([nums1[i],nums2[j]])

            if j+1 < len(nums2):
                heapq.heappush(H,( nums1[i]+nums2[j+1] , i, j+1))
        
        return ans

