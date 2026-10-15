class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        sub=[]
        for i in range(n):
            for j in range(i+1,n+1):
                sub.append(nums[i:j])
        for i in sub:
            x=len(set(i))
            res+=x**2
        return res