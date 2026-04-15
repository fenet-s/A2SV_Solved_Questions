from collections import Counter
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0
        for ans, count  in freq.items():
            group_size = ans + 1 
            groups = math.ceil(count/group_size)
            total += (groups * group_size)
        return total
            
        set_ = set(answers)
        set_l = list(set_)
        zero = answers.count(0)
        # 2,2,2,2,2
        if zero > 0:
            return sum(set_l) + len(set_l) + (zero-1)
        else:
            return sum(set_l) + len(set_l)
            