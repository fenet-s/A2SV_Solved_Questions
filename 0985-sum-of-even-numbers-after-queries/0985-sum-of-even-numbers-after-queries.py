class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        ans = []
        even_sum = sum(x for x in nums if x % 2 == 0)
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            
            nums[index] += val
            
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            ans.append(even_sum)
        
        return ans
