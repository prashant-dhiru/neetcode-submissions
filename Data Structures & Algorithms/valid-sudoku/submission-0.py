from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = 9
        n = 9
        
        seenRow = defaultdict(list)
        seenCol = defaultdict(list)
        seenSquare = defaultdict(list)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seenRow[r]:
                    return False
                if board[r][c] in seenCol[c]:
                    return False
                if board[r][c] in seenSquare[((r//3)*3) + (c//3)]:
                    return False

                seenRow[r].append(board[r][c])
                seenCol[c].append(board[r][c])
                seenSquare[(r//3)*3 + (c//3)].append(board[r][c])
        return True