class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""]*len(s)
        for idx, char in enumerate(s):
            target_idx = indices[idx]
            res[target_idx] = char
        return "".join(res)
        

        