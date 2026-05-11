class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        seenBox = defaultdict(set)
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if (num in seenRow[row] or num in seenCol[col]
                    or num in seenBox[(row//3,col//3)]):
                    return False
                
                seenRow[row].add(num)
                seenCol[col].add(num)
                seenBox[(row // 3,col // 3)].add(num)
        return True