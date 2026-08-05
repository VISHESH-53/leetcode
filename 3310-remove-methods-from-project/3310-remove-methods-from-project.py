from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n, k, edges):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        mark = [0] * n
        outsideConnection = False

        def bfs(color, src):
            nonlocal outsideConnection
            q = deque([src])
            mark[src] = color

            while q:
                node = q.popleft()

                for nxt in graph[node]:
                    if mark[nxt] == 1 and color == 2:
                        outsideConnection = True
                        return

                    if mark[nxt] != color:
                        mark[nxt] = color
                        q.append(nxt)

        bfs(1, k)

        for i in range(n):
            if i == k or mark[i] == 1:
                continue
            bfs(2, i)

        res = []

        for i in range(n):
            if not outsideConnection and mark[i] == 1:
                continue
            res.append(i)

        return res