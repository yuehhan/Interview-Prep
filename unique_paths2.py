<<<<<<< HEAD
def uniquePaths(self, m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    
=======
def uniquePaths(self, m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
    return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)