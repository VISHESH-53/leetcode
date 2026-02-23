class Solution(object):
    def hasAllCodes(self, s, k):
        x=1<<k
        if len(s) - k + 1 <x:
            return False
        
        seen =set()

        for i in range(len(s)-k+1):
            seen.add(s[i:i+k])
        return len(seen) == x
