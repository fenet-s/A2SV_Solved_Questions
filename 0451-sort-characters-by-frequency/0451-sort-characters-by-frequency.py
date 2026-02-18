from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = dict(sorted_items)
        ans = ""
        for key,value in sorted_dict.items():
            ans += key*value



        return ans

        