<<<<<<< HEAD
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = []
        index = 0
        self.generate(index, nums, current, res)
        return res

    
    def generate(self, index, nums, current, res):
        if current not in res:
            res.append(current)
            
        for i in range(index, len(nums)):
            self.generate(i+1, nums, current+[nums[i]], res)
=======
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = []
        index = 0
        self.generate(index, nums, current, res)
        return res

    
    def generate(self, index, nums, current, res):
        if current not in res:
            res.append(current)
            
        for i in range(index, len(nums)):
            self.generate(i+1, nums, current+[nums[i]], res)
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        