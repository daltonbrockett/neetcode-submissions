class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        curr = []
        def dfs(currIndex):
            if currIndex >= len(nums):
                out.append(curr.copy())
                return
            curr.append(nums[currIndex])
            dfs(currIndex + 1)
            curr.pop()
            dfs(currIndex + 1)
        dfs(0)
        return out
            
