class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,max(nums)+2):
            if i not in nums:
                missing_number=i
                return missing_number