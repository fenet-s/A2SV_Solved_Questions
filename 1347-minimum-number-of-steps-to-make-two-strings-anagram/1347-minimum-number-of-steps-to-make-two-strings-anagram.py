from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sorted_s= sorted(s)
        sorted_t = sorted(t)
        freq_s = Counter(sorted_s)
        freq_t = Counter(sorted_t)
        ans = 0
        for key, value in freq_s.items():
            if freq_s[key] - freq_t[key] > 0:
                ans += freq_s[key] - freq_t[key]
        return ans
             

        