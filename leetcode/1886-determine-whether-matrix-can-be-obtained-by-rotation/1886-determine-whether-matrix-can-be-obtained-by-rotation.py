class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        for x in range(4):
            for i in range(n):
                for j in range(i,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for row in mat:
                row.reverse()
            if mat==target:
                return True
            
        return False
        