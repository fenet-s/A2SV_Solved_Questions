class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        i = 0
        n = len(nums)-1
        while sum(nums) % k != 0:
            nums[i] = nums[i] -1
            counter += 1
            if i == n:
                i = 0
            else:
                i += 1
        return counter
        


       
        