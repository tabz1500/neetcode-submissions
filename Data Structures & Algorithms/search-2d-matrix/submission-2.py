class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while l <= r:
            mp = (l + r) // 2
            mprow = mp // cols
            mpcol = mp % cols

            if matrix[mprow][mpcol] == target:
                return True
            
            elif matrix[mprow][mpcol] < target:
                if mp < (rows * cols) - 1: l = mp + 1
                else: break

            else:
                if mp > 0: r = mp - 1
                else: break
        
        return False