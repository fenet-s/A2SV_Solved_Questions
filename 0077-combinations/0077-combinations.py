class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n + 1)]
        ans = []

        def backtrack(idx, combo):
            if len(combo) == k:
                ans.append(combo[:])
                return
            
            if idx == len(arr):
                return

            combo.append(arr[idx])
            backtrack(idx + 1, combo)
            combo.pop()

            backtrack(idx + 1, combo)

        backtrack(0, [])
        return ans
