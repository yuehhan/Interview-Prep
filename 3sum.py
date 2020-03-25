<<<<<<< HEAD
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            target = nums[i]*-1
            while j<k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                if nums[j] + nums[k] < target:
                    j+= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
            
        return res
    
=======
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            target = nums[i]*-1
            while j<k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                if nums[j] + nums[k] < target:
                    j+= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
            
        return res
    
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
