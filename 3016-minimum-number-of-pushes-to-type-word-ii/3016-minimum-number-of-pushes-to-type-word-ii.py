class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        for c in word:
            freq[ord(c) - ord('a')] += 1

        freq.sort()

        ans = 0
        idx = 0

        for f in reversed(freq):
            if f == 0:
                break
            ans += f * (idx // 8 + 1)
            idx += 1

        return ans