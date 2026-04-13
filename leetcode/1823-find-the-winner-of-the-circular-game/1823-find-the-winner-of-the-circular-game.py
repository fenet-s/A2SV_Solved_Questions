class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1, n + 1):
            arr.append(i)  # Append each person numbered from 1 to n
        
        i = 0
        while len(arr) > 1:
            i = (i + (k - 1)) % len(arr)  # Calculate the index to eliminate
            arr.pop(i)  # Remove the person at that index
        
        return arr[0]  # Return the last remaining person
