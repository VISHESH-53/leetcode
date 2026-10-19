class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        x=sum(cost)
        cost.sort()
        for i in range(len(cost)-3,-1,-3):
            x-=cost[i]
        return x
        