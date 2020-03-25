class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        
        ans = [[1],[1,1]]
        pascal = [1,1]
        while numRows > 2:
            temp = []
            for i in range(1,len(pascal)):
                temp.append(pascal[i-1]+pascal[i])
            
            temp.insert(0,1)
            temp.append(1)
            pascal = temp
            ans.append(temp)
            numRows -= 1
        
        return ans
                
            