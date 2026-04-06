class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            num = (l + r) // 2
            if nums[num] < target:
                l = num + 1
            elif nums[num] > target:
                r = num - 1
            else:
                return num
        return -1 