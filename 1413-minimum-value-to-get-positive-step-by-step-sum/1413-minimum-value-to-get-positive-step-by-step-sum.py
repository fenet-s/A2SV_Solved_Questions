class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        x = min(prefix)
        return abs(x) + 1

        