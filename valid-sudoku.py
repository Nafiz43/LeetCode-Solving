# day 01-Nafiz


from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):

                if board[row][col] is None or board[row][col] == ".":
                    continue
                if board[row][col] is not None:
                  if (board[row][col] in rows[row] or
                      board[row][col] in cols[col] or
                      board[row][col] in squares[(row // 3, col // 3)]):
                      return False
                  rows[row].add(board[row][col])
                  cols[col].add(board[row][col])
                  squares[(row//3, col//3)].add(board[row][col])
        return True


board = [["1","1",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

s = Solution().isValidSudoku(board)
print(s)
