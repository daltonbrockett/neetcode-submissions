class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSeen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numsSeen:
                return [numsSeen[diff], i]
            numsSeen[num] = i
        return []