class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                cs=nums[i]+nums[l]+nums[r]
                if cs==0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+ 1]:
                        l+=1
                    while l < r and nums[r] == nums[r- 1]:
                        r-=1
                    l += 1
                    r -=1
                elif cs<0:
                    l+=1
                else:
                    r-=1
        return res
            

        