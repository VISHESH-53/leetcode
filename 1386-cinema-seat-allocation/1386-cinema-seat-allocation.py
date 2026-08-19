from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, rs: list[list[int]]) -> int:
        d = defaultdict(set)
        for i in range(len(rs)):
            d[rs[i][0]].add(rs[i][1])

        empty_rows = n - len(d)
        ctr = empty_rows * 2

        c1 = {2, 3, 4, 5}
        c2 = {4, 5, 6, 7}
        c3 = {6, 7, 8, 9}

        for i in d:
            left_clear = c1.isdisjoint(d[i])
            middle_clear = c2.isdisjoint(d[i])
            right_clear = c3.isdisjoint(d[i])

            if left_clear and right_clear:
                ctr += 2
            elif left_clear or middle_clear or right_clear:
                ctr += 1

        return ctr
