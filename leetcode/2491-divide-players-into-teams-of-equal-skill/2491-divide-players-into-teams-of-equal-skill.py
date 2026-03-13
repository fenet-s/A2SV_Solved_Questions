class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l , r = 0 , len(skill)-1
        n = len(skill)
        mul_sum = 0
        skill.sort()
        while l<r and r <= n:
            target = skill[0] + skill[-1]
            if skill[l] + skill[r] == target:
                mul_sum += (skill[l]*skill[r])
                l += 1
                r -= 1
            else:
                return -1
        return mul_sum

        

        