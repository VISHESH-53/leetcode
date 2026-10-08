class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, ctr = [], 0

        for c in s:
            if c == ")":
                ctr -= 1
            if ctr > 0:
                res.append(c)
            if c == "(":
                ctr += 1
                
        return "".join(res)