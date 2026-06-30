class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for i, char in enumerate(s):
            last_seen[char] = i
            if -1 not in last_seen.values():
                count += 1 + min(last_seen.values())
                
        return count
