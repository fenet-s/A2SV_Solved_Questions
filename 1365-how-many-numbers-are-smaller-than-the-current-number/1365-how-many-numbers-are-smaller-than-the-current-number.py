class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        set_L= sorted(nums)
        res = []
        for num in nums:
            res.append(set_L.index(num))
        return res

        