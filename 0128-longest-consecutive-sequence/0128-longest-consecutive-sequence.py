class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedn = sorted(set(nums))
        if not nums:
            return 0

        current = 1
        longest = 0

        for i in range(1, len(sortedn)):
            if sortedn[i] == sortedn[i-1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)
