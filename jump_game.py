def canJump(self, nums: List[int]) -> bool:
    lastPosition = len(nums)-1
    for i in reversed(range(len(nums))):
        if i + nums[i] >= lastPosition:
            lastPosition = i

    return lastPosition == 0