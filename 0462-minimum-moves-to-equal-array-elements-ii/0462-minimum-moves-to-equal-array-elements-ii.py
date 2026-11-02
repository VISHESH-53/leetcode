class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        ctr=0
        while i<j:
            ctr+=nums[j]-nums[i]
            i+=1
            j-=1
        return ctr   

        