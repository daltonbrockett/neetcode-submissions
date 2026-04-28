class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)

        out[1] = 1
        for i in range(1, len(nums)):
            out[i] = nums[i - 1] * out[i-1]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= post 
            post *= nums[i]
        return out

            