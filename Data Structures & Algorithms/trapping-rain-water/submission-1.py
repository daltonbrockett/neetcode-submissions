class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        trapped = 0
        currLWall, currRWall = height[l], height[r]
        while l < r - 1:
            heightL, heightR, = height[l], height[r]
            if heightL >= heightR:
                r -= 1
                heightR = height[r]
                if heightR >= currRWall:
                    currRWall = heightR
                else:
                    trapped += currRWall - heightR
            else:
                l += 1
                heightL = height[l]
                if heightL >= currLWall:
                    currLWall = heightL
                else:
                    trapped += currLWall - heightL
        return trapped
            
        