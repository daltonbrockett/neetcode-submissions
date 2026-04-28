class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sety = set(nums)
        listy = sorted(list(sety))
        consec = 1
        currConsec = 1
        for i in range(0, len(listy) - 1):
            if listy[i] + 1 == listy[i + 1]:
                currConsec += 1
                if currConsec > consec:
                    consec = currConsec
            else:
                currConsec = 1
        return consec  