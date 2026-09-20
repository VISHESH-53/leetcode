class Solution:
    def reverseDegree(self, s: str) -> int:
        ans, idx = 0, 1
        for i in s:
            ans+= (123 - ord(i)) * idx
            idx+= 1

        return ans 
        
        