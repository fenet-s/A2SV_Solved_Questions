class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_ = sorted(people)
        boat = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if sorted_[left] + sorted_[right] <= limit:
                left += 1
            right -= 1
            boat += 1
        return boat
                        


      