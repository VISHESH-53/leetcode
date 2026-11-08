class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        cs = list(map(sum, zip(*grid)))
        return sum(
            rs
            for row in grid
            if (rs := sum(row))
            if rs > 1 or cs[row.index(1)] > 1
        )