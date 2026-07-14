class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        s=sum(nums)
        c=0
        for i in nums:
            c= max(c+i, i)
            if s<c:
                s=c
        return s


        