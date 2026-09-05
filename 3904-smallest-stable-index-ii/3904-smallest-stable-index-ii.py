class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prefixmax=[0]*n
        suffixmin=[0]*n
        prefixmax[0]=nums[0]
        for i in range(1,n):
            prefixmax[i]=max(prefixmax[i-1],nums[i])
        suffixmin[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suffixmin[i]=min(suffixmin[i+1],nums[i])
        for i in range(n):
            if prefixmax[i]-suffixmin[i]<=k:
                return i
        return -1