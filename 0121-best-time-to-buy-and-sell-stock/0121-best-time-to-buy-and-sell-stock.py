class Solution:
    def maxProfit(self, p: List[int]) -> int:
        mini=p[0]
        mxp=0
        for i in p:
            mxp=max(mxp,i -mini)
            mini=min(mini,i)
        return mxp


        
            
            
        