class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x=defaultdict(list)
        for i in strs:
            z="".join(sorted(i))
            x[z].append(i)
        return list(x.values())        