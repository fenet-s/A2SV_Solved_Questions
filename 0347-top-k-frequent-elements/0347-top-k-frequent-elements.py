from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= Counter(nums)
        sorted_ =sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [sorted_[i][0] for i in range(k)]
        

        