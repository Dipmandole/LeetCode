class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        # Maximum score
        score = [[-1] * n for _ in range(n)]

        # Number of ways
        ways = [[0] * n for _ in range(n)]

        # Start from S
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                best = -1
                cnt = 0

                # Down
                if i + 1 < n and score[i + 1][j] != -1:
                    if score[i + 1][j] > best:
                        best = score[i + 1][j]
                        cnt = ways[i + 1][j]
                    elif score[i + 1][j] == best:
                        cnt = (cnt + ways[i + 1][j]) % MOD

                # Right
                if j + 1 < n and score[i][j + 1] != -1:
                    if score[i][j + 1] > best:
                        best = score[i][j + 1]
                        cnt = ways[i][j + 1]
                    elif score[i][j + 1] == best:
                        cnt = (cnt + ways[i][j + 1]) % MOD

                # Diagonal
                if i + 1 < n and j + 1 < n and score[i + 1][j + 1] != -1:
                    if score[i + 1][j + 1] > best:
                        best = score[i + 1][j + 1]
                        cnt = ways[i + 1][j + 1]
                    elif score[i + 1][j + 1] == best:
                        cnt = (cnt + ways[i + 1][j + 1]) % MOD

                if best == -1:
                    continue

                val = 0
                if board[i][j].isdigit():
                    val = int(board[i][j])

                score[i][j] = best + val
                ways[i][j] = cnt % MOD

        if ways[0][0] == 0:
            return [0, 0]

        return [score[0][0], ways[0][0]]