<<<<<<< HEAD
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, zero = 0, len(nums)-1, 0
        while left <= right:
            if nums[left] == 0:
                nums[left], nums[zero] = nums[zero], nums[left]
                left += 1
                zero += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return nums
        
=======
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, zero = 0, len(nums)-1, 0
        while left <= right:
            if nums[left] == 0:
                nums[left], nums[zero] = nums[zero], nums[left]
                left += 1
                zero += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return nums
        
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
