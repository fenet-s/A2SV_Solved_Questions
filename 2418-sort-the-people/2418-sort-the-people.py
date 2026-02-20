class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_h = list(zip(names,heights))
        n = len(names)
        for _ in range(n):
            for i in range(n-1):
                if name_h[i][-1] < name_h[i+1][-1]:
                    name_h[i],name_h[i+1] = name_h[i+1],name_h[i]
        return [name for name,height in name_h]
        