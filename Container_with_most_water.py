def maxArea(self, height: List[int]) -> int:
    max_area = 0
    left, right = 0, len(height)-1

    while left < right:
        area = (min(height[left],height[right]))*len(range(left,right))
        if height[left] >= height[right]:
            right -= 1
        elif height[left] <= height[right]:
            left += 1
        if area>max_area:
            max_area = area

    return max_area
