class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postFix = [0 for _ in nums]
        post = 1
        for i, num in enumerate(reversed(nums)):
            post *= num
            postFix[len(nums) - i - 1] = post
        out = []
        pre = 1
        for i in range(len(nums) - 1):
            num = nums[i]
            out.append(pre * postFix[i + 1])
            pre *= num
        out.append(pre)
        return out