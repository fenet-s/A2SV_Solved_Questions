class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class LargerNum(str):
            def __lt__(x, y):
                return x + y < y + x

        strs = [str(num) for num in nums]
        
        strs.sort(key=LargerNum, reverse=True)
        
        ans = "".join(strs)
        
        return "0" if ans[0] == "0" else ans