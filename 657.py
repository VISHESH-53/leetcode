class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ctrL=0
        ctrR=0
        ctrU=0
        ctrD=0
        for i in moves:
            if i=="L":
                ctrL+=1
            elif i=="R":
                ctrR+=1
            elif i=="U":
                ctrU+=1
            elif i=="D":
                ctrD+=1
        if ctrD==ctrU and ctrL==ctrR:
            return True
        else:
            return False
        
