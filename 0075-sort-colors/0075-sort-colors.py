from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)

        zeros = freq.get(0, 0)
        ones = freq.get(1, 0)
        two = freq.get(2, 0)
        
      
        left = 0
        nums[left:left + zeros] = [0]* zeros
        left += zeros
        nums[left:left + ones] = [1] * ones
        left += ones
        nums[left:left + two] =[2] * two




        
        