class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)

        # Step 1: build difference array
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1

        # Step 2: prefix sum to get actual frequencies
        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq.pop()  # remove extra

        # Step 3: sort both
        nums.sort(reverse=True)
        freq.sort(reverse=True)

        # Step 4: compute result
        mod = 10**9 + 7
        res = 0

        for i in range(n):
            res = (res + nums[i] * freq[i]) % mod

        return res