class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0
        while l < r:
            height1 = heights[l]
            height2 = heights[r]
            vol = min(height1, height2) * (r-l)
            maximum = max(vol, maximum)
            if height1 > height2:
                r -= 1
            else:
                l += 1
        return maximum