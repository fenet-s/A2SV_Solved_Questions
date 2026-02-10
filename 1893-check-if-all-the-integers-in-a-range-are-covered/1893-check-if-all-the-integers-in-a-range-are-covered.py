from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        all_numbers = []

        for start, end in ranges:
            for i in range(start, end + 1):  
                all_numbers.append(i)

        for i in range(left, right + 1):
            if i not in all_numbers:
                return False

        return True

