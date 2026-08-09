class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        @cache
        def solve(person, i, M):
            if i >= n:
                return 0
                
            res = 0 if person == 1 else float('inf')
            stones = 0
            
            for x in range(1, min(2 * M, n - i) + 1):
                stones += piles[i + x - 1]
                
                if person == 1:
                    res = max(res, stones + solve(0, i + x, max(M, x)))
                else:
                    res = min(res, solve(1, i + x, max(M, x)))
                    
            return res
            
        return solve(1, 0, 1)