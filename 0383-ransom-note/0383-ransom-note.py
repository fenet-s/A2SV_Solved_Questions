class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_list = sorted(ransomNote)
        m_list = sorted(magazine)
        
        r_ptr = 0
        m_ptr = 0
        
        while r_ptr < len(r_list) and m_ptr < len(m_list):
            if r_list[r_ptr] == m_list[m_ptr]:
                r_ptr += 1
                m_ptr += 1
            else:
                m_ptr += 1
                
        return r_ptr == len(r_list)