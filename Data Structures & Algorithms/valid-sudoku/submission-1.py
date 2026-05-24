class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                if num > 10 or num < 1:
                    return False
                
                row = rows[i]
                col =  cols[j]
                squareidx = (i // 3) * 3 + (j // 3)
                square = squares[squareidx]
                mask = 1 << (num - 1)

                if (row & mask) or (col & mask) or (square & mask):
                    return False

                row |= mask
                col |= mask
                square |= mask

                rows[i] = row
                cols[j] = col
                squares[squareidx] = square
        
        return True



                