class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        index = 0
        current = []
        self.generate(candidates, target, index, current, res)
        return res
    
    def generate(self, candidates, target, index, current, res):
        if target == 0:
            res.append(current)
            return
        if target < 0:
            return
        
        for i in range(index, len(candidates)):
            self.generate(candidates, target-candidates[i], i, current+[candidates[i]], res)
        