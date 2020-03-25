<<<<<<< HEAD
# Given an array of numbers nums, in which exactly two elements 
# appear only once and all the other elements appear exactly twice. 
# Find the two elements that appear only once.


def singleNumber(nums):
    nums.sort()
    count = 0
    while len(nums) > 2:
        if nums[count] == nums[count+1]:
            nums.remove(nums[count])
            nums.remove(nums[count])
        else:
            count+= 1
    return nums

print(singleNumber([2,5,5,2,3,7,7,1]))
=======
# Given an array of numbers nums, in which exactly two elements 
# appear only once and all the other elements appear exactly twice. 
# Find the two elements that appear only once.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        count = 0
        while len(nums) > 2:
            if nums[count] == nums[count+1]:
                nums.remove(nums[count])
                nums.remove(nums[count])
            else:
                count+= 1
        return nums
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
