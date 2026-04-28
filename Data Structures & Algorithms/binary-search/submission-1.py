class Solution:
    def search(self, nums: List[int], target: int) -> int:
        back, front = 0, len(nums) - 1
        
        while back <= front:
            mid = (front + back) // 2
            
            if nums[mid] > target:
                front = mid - 1
            elif nums[mid] < target:
                back = mid + 1
            else:
                return mid
        return -1
