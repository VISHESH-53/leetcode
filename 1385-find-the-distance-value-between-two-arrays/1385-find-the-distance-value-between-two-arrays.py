class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ctr=0
        for i in arr1:
            for j in arr2:
                x=True
                if abs(i-j)<=d:
                    x=False
                    break
            if x==True:
                ctr+=1
        return ctr