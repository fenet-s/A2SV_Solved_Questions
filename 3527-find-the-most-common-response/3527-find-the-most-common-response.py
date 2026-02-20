from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        another = []
        for sub_ in responses:
            another.append(list(set(sub_)))
        flat_list = sum(another, [])
        frq =  Counter(flat_list)
        max_ = sorted(frq.items(), key=lambda x: (-x[1], x[0]))[0]
        return max_[0]
