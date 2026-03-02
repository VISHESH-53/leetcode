class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        back_zero_rows = [0] * n
        for i in range(n):
            back_zero_count = 0
            for x in reversed(grid[i]):
                if x == 0:
                    back_zero_count += 1
                else:
                    break
            back_zero_rows[i] = back_zero_count


        counter = 0
        for i in range(n):
            zero_needed = n-1-i

            if back_zero_rows[i] < zero_needed:
                for j in range(i + 1, n):
                    if back_zero_rows[j] >= zero_needed:
                        line = back_zero_rows.pop(j)
                        back_zero_rows.insert(i, line)
                        counter += j - i
                        break
                else:
                    return -1
        return counter
                    
