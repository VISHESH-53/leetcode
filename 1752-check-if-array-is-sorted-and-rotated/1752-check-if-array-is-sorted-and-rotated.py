class Solution:
    def check(self, nums: List[int]) -> bool:
        ctr=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                ctr+=1
        if nums[0]<nums[-1]:
            ctr+=1
            
        return ctr<=1     

        
        