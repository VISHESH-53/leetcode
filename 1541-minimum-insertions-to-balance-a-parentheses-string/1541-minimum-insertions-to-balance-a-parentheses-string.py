class Solution:
    def minInsertions(self, s: str) -> int:
        blc = ans = 0
        need = False

        for ch in s:
            if ch == '(':
                if need:
                    ans += 1
                    need = False

                blc += 1
            
            else:
                if need:
                    need = False
                else:
                    if blc == 0:
                        blc += 1
                        ans += 1
                
                    blc -= 1
                    need = True
        
        if need:
            ans += 1

        ans += blc * 2
        return ans