class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        x=len(nums)//2
        ctr1=0
        ctr2=0
        for i in range(x):
            z=nums[i]**2
            ctr1-=z
        for j in range(x,len(nums)):
            y=nums[j]**2
            ctr2+=y
        return ctr1+ctr2
        
        