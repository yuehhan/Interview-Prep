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
        
        return ''.join(res)