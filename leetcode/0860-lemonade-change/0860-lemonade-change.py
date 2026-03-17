class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for change in bills:
            if change == 5:
                five += 1

            elif change == 10:
                five -= 1
                ten += 1
                if five < 0:
                    return False

            else: 
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3

                if five < 0:
                    return False

        return True
