class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            numL = numbers[l]
            numR = numbers[r]
            sumNum = numL + numR
            if sumNum == target:
                return [l + 1, r + 1]
            if sumNum < target:
                l += 1
            else:
                r -= 1
        return []
