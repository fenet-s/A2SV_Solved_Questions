from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        count = Counter(changed)
        ans = []

        for num in changed:
            if count[num] == 0:
                continue
            
            if count[2 * num] == 0:
                return []
            
            ans.append(num)
            count[num] -= 1
            count[2 * num] -= 1

        return ans
