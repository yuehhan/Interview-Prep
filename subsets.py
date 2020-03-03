# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        index = 0
        self.generate(index, nums, current, res)
        return res
    
    def generate(self, index, nums, current, res):
        res.append(current)
        
        for i in range(index, len(nums)):
            self.generate(i+1, nums, current+[nums[i]], res)
            
            

