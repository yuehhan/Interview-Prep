def numIslands(self, grid: List[List[str]]) -> int:
class Solution:
    def defangIPaddr(self, address: str) -> str:
        myaddress = ""
        for i in address:
            if i != ".":
                myaddress += i
            else:
                myaddress += "[.]"
        return myaddress        
