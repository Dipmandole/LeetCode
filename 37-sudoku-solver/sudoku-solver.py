class Solution(object):
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for i in range(9):
            for j in range(9):

                if board[i][j] != ".":
                    dig = board[i][j]
                    box = (i // 3) * 3 + (j // 3)

                    rows[i].add(dig)
                    cols[j].add(dig)
                    boxes[box].add(dig)

        def isSafe(row, col, dig):

            box = (row // 3) * 3 + (col // 3)

            if dig in rows[row]:
                return False

            if dig in cols[col]:
                return False

            if dig in boxes[box]:
                return False

            return True

        def helper():

            # Find the empty cell with minimum possibilities
            bestRow = -1
            bestCol = -1
            minCount = 10

            for row in range(9):
                for col in range(9):

                    if board[row][col] == ".":

                        count = 0

                        for dig in "123456789":

                            if isSafe(row, col, dig):
                                count += 1

                        if count == 0:
                            return False

                        if count < minCount:
                            minCount = count
                            bestRow = row
                            bestCol = col

                            # Only one possible number
                            if minCount == 1:
                                break

                if minCount == 1:
                    break

            # No empty cells
            if bestRow == -1:
                return True

            # Try digits
            for dig in "123456789":

                if isSafe(bestRow, bestCol, dig):

                    box = (bestRow // 3) * 3 + (bestCol // 3)

                    # Place digit
                    board[bestRow][bestCol] = dig
                    rows[bestRow].add(dig)
                    cols[bestCol].add(dig)
                    boxes[box].add(dig)

                    if helper():
                        return True

                    # Backtracking
                    board[bestRow][bestCol] = "."
                    rows[bestRow].remove(dig)
                    cols[bestCol].remove(dig)
                    boxes[box].remove(dig)

            return False

        helper()