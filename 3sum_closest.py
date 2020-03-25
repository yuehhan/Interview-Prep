<<<<<<< HEAD
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            left,right = i+1, len(nums)-1
            while left < right:
                mysum = nums[i]+nums[left]+nums[right]
                if abs(target-mysum) < abs(target-result):
                    result = mysum
                if mysum < target:
                    left += 1
                elif mysum > target:
                    right -= 1
                else:
                    return result
        
        return result
=======
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            left,right = i+1, len(nums)-1
            while left < right:
                mysum = nums[i]+nums[left]+nums[right]
                if abs(target-mysum) < abs(target-result):
                    result = mysum
                if mysum < target:
                    left += 1
                elif mysum > target:
                    right -= 1
                else:
                    return result
        
        return result
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
