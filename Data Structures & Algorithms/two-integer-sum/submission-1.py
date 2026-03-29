class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previewsMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in previewsMap:
                return [previewsMap[diff],i]
            previewsMap[n] = i