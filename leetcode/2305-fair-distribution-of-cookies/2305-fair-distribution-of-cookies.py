class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childs = [0] *k
        
        self.minUnfairness = float('inf')
        
        def backtrack(idx, max_so_far):
            if max_so_far > self.minUnfairness:
                return 
            if idx == len(cookies):
                self.minUnfairness = min(self.minUnfairness , max(childs))
                return 
             
            for i in range(k):
                childs[i] += cookies[idx]
                backtrack(idx+1, max(max_so_far, max(childs)))
                childs[i] -= cookies[idx]
        backtrack(0,0)

        return self.minUnfairness
        