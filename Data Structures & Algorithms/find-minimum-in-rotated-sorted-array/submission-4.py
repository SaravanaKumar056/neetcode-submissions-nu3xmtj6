class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1 
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            res = min(res, nums[mid])
        return res