<<<<<<< HEAD
def canJump(self, nums: List[int]) -> bool:
    lastPosition = len(nums)-1
    for i in reversed(range(len(nums))):
        if i + nums[i] >= lastPosition:
            lastPosition = i

=======
def canJump(self, nums: List[int]) -> bool:
    lastPosition = len(nums)-1
    for i in reversed(range(len(nums))):
        if i + nums[i] >= lastPosition:
            lastPosition = i

>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
    return lastPosition == 0