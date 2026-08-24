class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [i for y in matrix for i in y]
        
        l = 0
        r = len(arr)

        while l <= r:
            mp = (l + r) // 2

            if arr[mp] == target:
                return True
            
            elif arr[mp] < target:
                if mp < len(arr) - 1: l = mp + 1
                else: break

            else:
                if mp > 0: r = mp - 1
                else: break
        
        return False