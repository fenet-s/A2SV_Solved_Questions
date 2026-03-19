class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            ans = []
            number = 0
            while index < len(s):
                char = s[index]
                # number
                if char.isdigit():
                    number = (number * 10) +  int(char)
                elif char == "[":
                    decoded, new_index = helper(index + 1)
                    ans.append(decoded * number)

                    number = 0
                    index = new_index
                elif char == "]":
                    return "".join(ans), index 
                else:
                    ans.append(char)
                index += 1
            return "".join(ans)
        
        return helper(0)