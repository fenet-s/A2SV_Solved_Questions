from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        n = len(p)
        m = len(s)
        
        if n > m:
            return ans
        
        p_count = Counter(p)
        window_count = Counter(s[:n])
        
        if window_count == p_count:
            ans.append(0)
        
        for i in range(n, m):
            window_count[s[i]] += 1
            
            window_count[s[i - n]] -= 1
            if window_count[s[i - n]] == 0:
                del window_count[s[i - n]]
            
            if window_count == p_count:
                ans.append(i - n + 1)
        
        return ans