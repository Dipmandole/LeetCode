from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x):
            if x <= 0:
                return 0

            s = str(x)
            n = len(s)

            @lru_cache(None)
            def dp(pos, prev1, prev2, tight, started):

                # End of number
                if pos == n:
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_count = 0
                total_wavy = 0

                for d in range(limit + 1):

                    new_tight = tight and (d == limit)

                    # still leading zeros
                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            -1,
                            -1,
                            new_tight,
                            False
                        )

                        total_count += cnt
                        total_wavy += wav

                    else:

                        add = 0

                        # We have 3 digits: prev2 prev1 d
                        if prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or \
                               (prev1 < prev2 and prev1 < d):
                                add = 1

                        cnt, wav = dp(
                            pos + 1,
                            d,
                            prev1,
                            new_tight,
                            True
                        )

                        total_count += cnt
                        total_wavy += wav + add * cnt

                return (total_count, total_wavy)

            return dp(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)        