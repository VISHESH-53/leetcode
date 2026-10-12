class Solution:
    def findDelayedArrivalTime(self, aT: int, dT: int) -> int:
        if (aT+dT)>=24:
            return (aT+dT)-24
        else:
            return aT+dT
        