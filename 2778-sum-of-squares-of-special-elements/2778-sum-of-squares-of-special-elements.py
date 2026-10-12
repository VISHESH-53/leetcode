class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        ctr=0
        for i in range(n):
            p=i+1
            if n%p==0:
                x=nums[i]**2
                ctr+=x
        return ctr

        