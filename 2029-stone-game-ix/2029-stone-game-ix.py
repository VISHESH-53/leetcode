class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        c1 = sum(1 for x in stones if x % 3 == 1)
        c2 = sum(1 for x in stones if x % 3 == 2)
        c0 = len(stones) - c1 - c2

        if c0 & 1 == 0:
            return c1 > 0 and c2 > 0
            
        return abs(c1 - c2) > 2
