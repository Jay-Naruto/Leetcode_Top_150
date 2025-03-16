class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_map = collections.defaultdict(int)
        max_l = 0
        max_freq = 0
        l=0
        for r in range(len(s)):
            c_map[s[r]] += 1
            max_freq = max(max_freq, c_map[s[r]])
            while (r-l + 1) - max_freq > k:
                c_map[s[l]] -= 1
                l+=1
            max_l = max(max_l, r-l+1)
        return max_l
        