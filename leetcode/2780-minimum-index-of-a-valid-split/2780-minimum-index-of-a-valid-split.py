from typing import List
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find dominant candidate (Boyer-Moore)
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Step 2: Count total occurrences
        total = nums.count(candidate)
        n = len(nums)
        
        # If no dominant element
        if total <= n // 2:
            return -1
        
        # Step 3: Try splits
        left_count = 0
        
        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1
            
            right_count = total - left_count
            
            # Check dominance
            if left_count > (i + 1) // 2 and right_count > (n - i - 1) // 2:
                return i
        
        return -1