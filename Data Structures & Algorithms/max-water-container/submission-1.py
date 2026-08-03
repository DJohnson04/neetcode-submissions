class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water_amount = 0
        while left < right:
            temp = min(heights[left], heights[right]) * (right - left)
            if temp > water_amount:
                water_amount = temp
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return water_amount