class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, n in enumerate(nums):
            index[n] = i
        
        for i, n in enumerate(nums):
            different = target - n

            if different in index and index[different] != i:
                return [i, index[different]]
        return []