class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        ans=""
        for i in s:
            if i=="(":
                stack.append(ans)
                ans=""
            elif i==")":
                ans=ans[::-1]
                ans=stack.pop()+ans
            else:
                ans+=i
        return ans
