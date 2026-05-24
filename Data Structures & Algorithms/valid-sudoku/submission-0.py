class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                if num > 10 or num < 1:
                    return False
                
                row = rows.get(i, set())
                col = cols.get(j, set())
                squareidx = (i // 3) * 3 + (j // 3)
                square = squares.get(squareidx, set())

                if num in row or num in col or num in square:
                    return False

                row.add(num)
                col.add(num)
                square.add(num)

                rows[i] = row
                cols[j] = col
                squares[squareidx] = square
        
        return True



                