class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx=0
        for i in range(len(nums)):
            step=max(mx-1,nums[i])
            if step <= 0 and i !=len(nums)-1:
                return False
            mx = step 
        return True