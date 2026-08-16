class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]
        
        for x in stones:
            cnt[x % 3] += 1
            
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]

        if c0 & 1 == 0:
            return c1 > 0 and c2 > 0
            
        return c1 - c2 > 2 if c1 > c2 else c2 - c1 > 2
