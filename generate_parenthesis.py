<<<<<<< HEAD
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return []
        res = []
        open = n
        close = n
        string = ""
        self.generate(res, open, close, string)
        return res
    
    def generate(self, res, open, close, string):
        if open > close or open < 0 or close < 0:
            return
        if open == 0 and close == 0:
            res.append(string)
            return
        
        self.generate(res, open-1, close, string+'(')
        self.generate(res, open, close-1, string+')')
=======
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return []
        res = []
        open = n
        close = n
        string = ""
        self.generate(res, open, close, string)
        return res
    
    def generate(self, res, open, close, string):
        if open > close or open < 0 or close < 0:
            return
        if open == 0 and close == 0:
            res.append(string)
            return
        
        self.generate(res, open-1, close, string+'(')
        self.generate(res, open, close-1, string+')')
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
