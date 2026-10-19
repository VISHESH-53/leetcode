class Solution:
    def minElement(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            x=str(i)
            ctr=0
            for j in x:
                ctr+=int(j)
            l.append(ctr)
        return min(l)
            