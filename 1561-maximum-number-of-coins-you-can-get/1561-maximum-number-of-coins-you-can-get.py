class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        n = len(piles) // 3
        coins = 0
        
        index = len(piles) - 2 
        
        for _ in range(n):
            coins += piles[index]
            index -= 2   
        return coins