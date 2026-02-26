class Solution(object):
    def numSteps(self, s):
        x=int(s,2)
        ctr=0
        while x!=1:
            
            if x%2==0:
                x=x/2
            else:
                x=x+1
            ctr+=1
        return ctr
            

        
