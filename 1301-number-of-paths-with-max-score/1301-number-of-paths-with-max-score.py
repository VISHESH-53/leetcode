class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        grid = []
        self.dp = {}
        for i in range(len(board)) :
            row = list(board[i])
            for k in range(len(row)) :
                row[k] = -1 if row[k] == 'X' else int(row[k]) if row[k] >= '1' and row[k] <= '9' else 0
            grid.append(row)
        
        def dfsUtil(i, j) :
            if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1 :
                return (float(-inf), float(-inf))

            if i == len(grid)-1 and j == len(grid)-1 :
                return (0, 1)

            if (i, j) in self.dp :
                return self.dp[(i, j)]

            down = dfsUtil(i+1, j)
            right = dfsUtil(i, j+1)
            diagonal = dfsUtil(i+1, j+1)

            max_sum = max(down[0], max(right[0], diagonal[0]))
            total_paths = 0

            total_paths += down[-1] if down[0] == max_sum else 0
            total_paths += right[-1] if right[0] == max_sum else 0
            total_paths += diagonal[-1] if diagonal[0] == max_sum else 0

            self.dp[(i, j)] = [max_sum+grid[i][j], total_paths]
            return [max_sum+grid[i][j], total_paths] 

        max_sum, paths = dfsUtil(0, 0)
        return [max_sum % ((10 ** 9) + 7), paths % ((10 ** 9) + 7)] if max_sum != float(-inf) else (0, 0)