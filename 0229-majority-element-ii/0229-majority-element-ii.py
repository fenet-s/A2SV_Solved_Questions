from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = []
        n = len(nums)
        for key,value in freq.items():
            if value > n//3:
                ans.append(key)
        return ans

        