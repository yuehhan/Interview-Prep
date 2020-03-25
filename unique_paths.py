<<<<<<< HEAD
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for j in range(m)] for i in range(n)]
        
        for j in range(1,m):
            for i in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
=======
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for j in range(m)] for i in range(n)]
        
        for j in range(1,m):
            for i in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return matrix[n-1][m-1]