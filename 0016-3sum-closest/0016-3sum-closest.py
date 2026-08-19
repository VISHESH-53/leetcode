class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-1):
            l=i+1
            r=len(nums)-1
            while l<r:
                x=nums[i]+nums[l]+nums[r]
                if abs(target-x)<abs(target-ans):
                    ans=x
                if x<target:
                    l+=1
                elif x>target:
                    r-=1
                else:
                    return x
        return ans
                


        