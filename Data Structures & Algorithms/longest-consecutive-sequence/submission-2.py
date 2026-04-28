class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sety = set(nums)
        count = 1

        for integer in sety:
            if (integer - 1) not in sety:
                tempCount = 1
                while (integer + tempCount) in sety:
                    tempCount += 1
                if tempCount > count:
                    count = tempCount
        return count