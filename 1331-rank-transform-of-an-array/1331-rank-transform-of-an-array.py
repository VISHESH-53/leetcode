class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=sorted(list(set(arr)))
        r={}
        for i,n in enumerate(temp):
            r[n]=i+1
        return [r[n] for n in arr]
        


                    
            
