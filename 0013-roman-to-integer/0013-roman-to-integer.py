class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5,"X": 10, "L":50, "C":100, "D":500, "M":1000}

        last = 0
        res = 0
        for i in s[::-1]:
            if roman[i] >= last:
                res += roman[i]
                last = roman[i]
            else:
                res -= roman[i]
        return res