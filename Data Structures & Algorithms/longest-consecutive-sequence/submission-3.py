class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = 0
        numsSet = set()
        for num in nums:
            numsSet.add(num)
        
        for num in numsSet:
            if num - 1 not in numsSet:
                currRun = 1
                while num + 1 in numsSet:
                    num = num + 1
                    currRun +=1
                out = max(currRun, out)
        return out
