class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l=[]
        n=len(nums[0])
        for i in nums:
            x=int(i,2)
            l.append(x)
        v=(2**n)-1
        for i in range(v+1):
            if i not in l:
                return format(i, f'0{n}b')
            
        
