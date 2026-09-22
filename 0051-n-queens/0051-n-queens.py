class Solution(object):
    def solveNQueens(self, n):
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        
        def isSafe(row, col):
            #Horizontal
            for i in range(row):
                if board[row][i] == "Q":
                    return False
            #Vertical
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            #Check upper-left diagonal
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            # Check upper-right diagonal
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        def nQueens(row):
            # Base Condition
            if row == n:
                solution = []
                for r in board:
                    solution.append("".join(r))
                ans.append(solution)
                return

            # Every index, Col
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    nQueens(row + 1)
                    board[row][col] = '.'
        nQueens(0)
        return ans

        
        """
        :type n: int
        :rtype: List[List[str]]
        """
        