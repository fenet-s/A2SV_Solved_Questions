class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)
        for shift in shifts:
            direction = 1
            if shift[2] == 0:
                direction = -1
            prefix_sum[shift[0]] += direction
            prefix_sum[shift[1]+1] -= direction
        
        for i in range(1,len(s)):
            prefix_sum[i] += prefix_sum[i-1]
        
        ans = []
        for i in range(len(s)):
            new_ord = (ord(s[i]) + prefix_sum[i] - ord('a'))%26 +ord('a')
            ans.append(chr(new_ord))
        
        return "".join(ans)