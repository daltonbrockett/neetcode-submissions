class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postFix = [0] * len(nums)
        post = 1
        for i, num in enumerate(reversed(nums)):
            post *= num
            postFix[len(nums) - i - 1] = post
        out = [0] * len(nums)
        pre = 1
        for i in range(len(nums) - 1):
            num = nums[i]
            out[i] = (pre * postFix[i + 1])
            pre *= num
        out[len(nums) - 1] = pre
        return out