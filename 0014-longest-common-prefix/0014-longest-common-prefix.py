class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = ""
        target = strs[0]
        
        for left in range(len(target)):
            for i in range(len(strs)):
                if left >= len(strs[i]) or strs[i][left] != target[left]:
                    return check
            
            check += target[left]
        
        return check
