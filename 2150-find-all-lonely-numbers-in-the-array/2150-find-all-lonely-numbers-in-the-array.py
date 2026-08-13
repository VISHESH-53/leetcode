class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = dict(Counter(nums))
        l=[]
        for i in freq:
            if freq[i]==1 and (i+1) not in freq and (i-1) not in freq:
                l.append(i)
        return l
                    
        