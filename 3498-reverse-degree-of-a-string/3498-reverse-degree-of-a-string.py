class Solution:
    def reverseDegree(self, s: str) -> int:
        ctr=0
        x=ord('z')
        for i in range(len(s)):
            
            ctr+=(x-ord(s[i])+1)*(i+1)
        return ctr
        
        