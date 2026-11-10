class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        arr=[]
        for i in nums:
            ctr=0
            for j in nums:
                if i>j:
                    ctr+=1
            arr.append(ctr)
        return arr
        