<<<<<<< HEAD
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        if numRows > len(s):
            return s
            
        
        res = ['']*numRows
        forward = 1
        index = 0
        
        for x in s:
            res[index] += x
            if index == 0:
                forward = 1
            elif index == numRows-1:
                forward = -1
            index += forward
        
=======
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        if numRows > len(s):
            return s
            
        
        res = ['']*numRows
        forward = 1
        index = 0
        
        for x in s:
            res[index] += x
            if index == 0:
                forward = 1
            elif index == numRows-1:
                forward = -1
            index += forward
        
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return ''.join(res)