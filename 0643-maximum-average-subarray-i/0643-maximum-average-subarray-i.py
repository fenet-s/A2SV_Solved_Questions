class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       initial_window = sum(nums[:k])
       max_window = initial_window
       n = len(nums)
       i = 0
       while i + k < n:
        new_window = initial_window + (nums[i+k] - nums[i])
        max_window = max(max_window, new_window) 
        initial_window = new_window
        i += 1
       return max_window/k





        