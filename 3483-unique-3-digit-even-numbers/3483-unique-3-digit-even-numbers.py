class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        for a in range(1, 10):         
            if freq[a] == 0:
                continue

            freq[a] -= 1

            for b in range(10):        
                if freq[b] == 0:
                    continue

                freq[b] -= 1

                for c in range(0, 10, 2): 
                    if freq[c] > 0:
                        ans += 1

                freq[b] += 1

            freq[a] += 1

        return ans