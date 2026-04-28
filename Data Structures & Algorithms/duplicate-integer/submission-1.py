class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapy = {}
        for num in nums:
            if num in mapy:
                return True
            else:
                mapy[num] = 1
        return False
        