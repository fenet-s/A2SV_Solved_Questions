class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = sorted(nums)
        left, right = 0, len(num) - 1

        while left < right:
            s = num[left] + num[right]

            if s == target:
                if num[left] == num[right]:
                    i = nums.index(num[left])
                    j = nums.index(num[right], i + 1)
                else:
                    i = nums.index(num[left])
                    j = nums.index(num[right])
                return [i, j]

            elif s > target:
                right -= 1
            else:
                left += 1
