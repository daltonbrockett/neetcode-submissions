class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        subset = []
        def backtracking(index: int):
            if index >= len(nums):
                out.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtracking(index + 1)
            subset.pop()
            backtracking(index + 1)

        backtracking(0)

        return out
