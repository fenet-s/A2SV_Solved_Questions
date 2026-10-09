class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 3**19
        if n > 0 and power % n  == 0:
            return True
        else:
            return False

        