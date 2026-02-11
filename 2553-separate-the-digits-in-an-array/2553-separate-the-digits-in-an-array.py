class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        final = []
        for num in nums:
            # Convert number to string to iterate through digits
            st = str(num) 
            for char in st:
                # Convert character back to integer and add to final list
                final.append(int(char))
        return final