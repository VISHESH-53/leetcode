class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        ans=[]
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                ans.append(i)
                break

        if ans ==[]:
            return [-1,-1]
        return ans

        