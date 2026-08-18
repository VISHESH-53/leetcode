class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=min(strs,key=len)
        ctr=0
        ans=""
        for i in range(len(x)):
            r=[j[ctr]for j in strs]
                
            all_same = len(set(r)) == 1
            if all_same:
                ans=ans+strs[0][ctr]
                ctr+=1
            else:
                return ans
        return ans

