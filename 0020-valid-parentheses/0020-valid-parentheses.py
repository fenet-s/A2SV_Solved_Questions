class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            
            elif char in mapping:
                if not stack:
                    return False
                
                top_item = stack.pop()
                
                if top_item != mapping[char]:
                    return False
                    
       
        return len(stack) == 0