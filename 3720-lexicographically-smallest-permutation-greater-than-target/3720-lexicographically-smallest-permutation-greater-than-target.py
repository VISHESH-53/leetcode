
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        
        for i in range(n - 1, -1, -1):
            f = freq.copy()
            possible = True
            
            for j in range(i):
                if f[target[j]] <= 0:
                    possible = False
                    break
                f[target[j]] -= 1
                
            if not possible:
                continue
                
            for choice in sorted(f.keys()):
                if choice > target[i] and f[choice] > 0:
                    ans = target[:i] + choice
                    f[choice] -= 1
                    
                    for char in sorted(f.keys()):
                        ans += char * f[char]
                    return ans
                    
        return ""