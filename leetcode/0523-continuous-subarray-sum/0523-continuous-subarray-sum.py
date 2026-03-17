class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        current_sum = 0
        seen = {0: -1}  

        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k

            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i

        return False