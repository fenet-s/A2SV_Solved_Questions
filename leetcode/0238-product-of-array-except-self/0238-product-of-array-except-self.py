class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # prefix product
        pre = 1
        for i in range(n):
            result[i] = pre
            pre *= nums[i]
        
        # suffix product
        suf = 1
        for i in range(n-1, -1, -1):
            result[i] *= suf
            suf *= nums[i]
        
        return result