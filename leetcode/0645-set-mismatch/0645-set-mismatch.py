class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]):
        count = Counter(nums)
        
        duplicates = []
        missing = []
        
        n = len(nums)
        
        for i in range(1, n + 1):
            if count[i] == 0:
                missing.append(i)
            elif count[i] > 1:
                duplicates.append(i)
        
        return [*duplicates, *missing]