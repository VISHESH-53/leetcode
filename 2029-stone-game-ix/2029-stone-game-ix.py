class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = {0: 0, 1: 0, 2: 0}
        
        for x in stones:
            cnt[x % 3] += 1
            
        if cnt[0] % 2 == 0:
            return min(cnt[1], cnt[2]) > 0
            
        return abs(cnt[1] - cnt[2]) > 2
