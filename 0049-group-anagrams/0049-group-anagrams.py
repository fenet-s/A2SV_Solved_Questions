class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in strs:
            key="".join(sorted(i))
            if key not in dict1:
                dict1[key]=[]
            dict1[key].append(i)
        return list(dict1.values())
