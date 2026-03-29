class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy_set = set(nums.copy())
        if len(copy_set) == len(nums):
            return False
        return True