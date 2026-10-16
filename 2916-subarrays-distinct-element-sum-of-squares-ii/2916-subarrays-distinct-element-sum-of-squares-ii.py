class Solution:
    def sumCounts(self, nums):
        last = {}  # last occurrence of a value
        idxs = []  # indices of last occurrences, sorted
        totalsum = curr = ans = 0
        for i, x in enumerate(nums):
            j = last.get(x, -1)
            small = 0 if j < 0 else bisect_right(idxs, j)  # entries <= j
            large = len(idxs) - small  # entries > j
            s = totalsum - sum(idxs[:small]) if small <= large else sum(idxs[small:])
            curr += 2 * (s - j * large) + i - j
            if j >= 0:
                del idxs[small - 1]  # idxs[small-1] == j
                totalsum -= j
            idxs.append(i)
            totalsum += i
            last[x] = i
            ans += curr
        return ans % 1_000_000_007