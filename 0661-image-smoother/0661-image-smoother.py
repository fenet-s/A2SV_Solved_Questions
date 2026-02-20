class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        Row = len(img)
        Col = len(img[0])
        matrix = copy.deepcopy(img)
        def isValid(r,c):
            return 0 <= r < Row and 0 <= c < Col
        def surroundingSum(r,c):
            total_sum = img[r][c]
            count = 1
            neighbors = [
                    (r-1, c-1),  # top-left
                    (r-1, c),    # top
                    (r-1, c+1),  # top-right
                    (r,   c-1),  # left
                    (r,   c+1),  # right
                    (r+1, c-1),  # bottom-left
                    (r+1, c),    # bottom
                    (r+1, c+1)   # bottom-right
                ] 
            for row,col in neighbors:
                if isValid(row,col):
                    total_sum += img[row][col]
                    count += 1
            return total_sum // count
        for r in range(Row):
            for c in range(Col):
                matrix[r][c] = surroundingSum(r,c)
        return matrix