class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        column = []

        for i in range(len(matrix)):
            if 0 in matrix[i]:
                row.append(i) 

        for j in row:
            for i in range(len(matrix[j])):
                if matrix[j][i] == 0:
                    column.append(i)


            matrix[j] = [0] * len(matrix[j])

        for j in matrix:
            for k in column:
                j[k] = 0 
        