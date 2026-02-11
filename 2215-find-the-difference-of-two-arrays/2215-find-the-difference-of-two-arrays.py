class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        ans2 =[]
        ans1 = set(nums1) - set(nums2)
        ans2 = set(nums2) - set(nums1)
        return [list(ans1), list(ans2)
]
        

        