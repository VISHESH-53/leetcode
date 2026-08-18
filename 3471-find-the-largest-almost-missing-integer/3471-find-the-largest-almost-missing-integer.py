class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        count=dict.fromkeys(nums, 0)
        l=[]
        for i in range(len(nums)-k+1):
            x=set(nums[i:i+k])
            for j in x:
                count[j]+=1
        for i in count:
            if count[i]==1:
                l.append(i)
        if len(l)==0:
            return -1
        return max(l)

        