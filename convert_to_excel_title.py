class Solution:
    def convertToTitle(self, n: int) -> str:
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ""
        while n > 0:
            n = n-1
            ans = alph[n%26] + ans
            n = n//26
        return ans
