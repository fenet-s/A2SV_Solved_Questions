from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        left = []
        right = []

        for sub_list in matches:
            left.append(sub_list[0])    
            right.append(sub_list[1])  

        count = Counter(right)  

        
        winners = [player for player in set(left) if player not in count]

       
        loser_once = [player for player in count if count[player] == 1]

        return [sorted(winners), sorted(loser_once)]
