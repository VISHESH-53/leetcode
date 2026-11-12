class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mx=1
        si=1
        sd=1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                si+=1
                sd=1
            elif nums[i]>nums[i-1]:
                sd+=1
                si=1
            else:
                si=1
                sd=1
            mx=max(mx,si,sd)
        return mx

        