class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0
        
        for word in words:
            # Checks every character in the word
            can_form = True
            for char in word:
                # If the word needs more of 'char' than available in 'chars'
                if word.count(char) > chars.count(char):
                    can_form = False
                    break
            
            # If we passed the check, add the LENGTH of the word
            if can_form:
                total_length += len(word)

        return total_length