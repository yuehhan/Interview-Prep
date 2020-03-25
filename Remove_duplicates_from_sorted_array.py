class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 3
        while j <= len(nums):
            if nums[i:j] == [nums[i]]*3:
                nums.remove(nums[i])
            else:
                i+=1
                j+=1
        return len(nums)