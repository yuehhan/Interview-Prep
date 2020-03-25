<<<<<<< HEAD
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 3
        while j <= len(nums):
            if nums[i:j] == [nums[i]]*3:
                nums.remove(nums[i])
            else:
                i+=1
                j+=1
=======
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 3
        while j <= len(nums):
            if nums[i:j] == [nums[i]]*3:
                nums.remove(nums[i])
            else:
                i+=1
                j+=1
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return len(nums)