class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle = num//3
        first = middle -1
        last = middle + 1
        if sum([first,middle,last]) == num:
            return [first,middle,last]
        else:
            return []
        