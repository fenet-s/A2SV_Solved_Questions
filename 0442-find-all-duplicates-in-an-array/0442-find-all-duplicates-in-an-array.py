from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        frq = Counter(nums)
        res = []
        for key, value in frq.items():
            if value == 2:
                res.append(key)
        return res

        