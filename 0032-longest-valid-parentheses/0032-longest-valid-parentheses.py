class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ctr=0
        stack=[-1]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ctr=max(ctr,i- stack[-1])
        return ctr