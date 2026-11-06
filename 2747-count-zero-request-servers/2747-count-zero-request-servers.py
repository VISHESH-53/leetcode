class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda a: a[1])

        q = sorted([(val, i) for i, val in enumerate(queries)])

        ans = [0] * len(queries)

        freq = {}
        left = 0
        right = 0
        m = len(logs)

        for time, idx in q:

            start = time - x

            # Add logs within the right boundary
            while right < m and logs[right][1] <= time:
                server = logs[right][0]
                freq[server] = freq.get(server, 0) + 1
                right += 1

            # Remove logs before the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            ans[idx] = n - len(freq)

        return ans