class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack=[]
        i=0
        j=1
        while i<len(target):
            stack.append("Push")
            if j==target[i]:
                i+=1
            else:
                stack.append("Pop")
            j+=1
        return stack