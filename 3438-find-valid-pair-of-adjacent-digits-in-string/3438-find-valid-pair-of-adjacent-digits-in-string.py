from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        # 1. Count the frequency of every character in the string
        freq = Counter(s)
        
        # 2. Iterate through the string to find adjacent pairs
        # We stop at len(s) - 1 because we are looking at i and i+1
        for i in range(len(s) - 1):
            first = s[i]
            second = s[i+1]
            
            if first != second:
                if freq[first] == int(first) and freq[second] == int(second):
                    return first + second
        
        return ""