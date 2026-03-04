class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m=len(mat)
        n=len(mat[0])
        row=[0]*m
        col=[0]*n
        ctr=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    row[i] +=1
                    col[j] +=1
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ctr += 1
        return ctr

            
                    


        
