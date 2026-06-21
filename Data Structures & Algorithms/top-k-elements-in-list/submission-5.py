class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        bucket = [[] for i in range(len(nums) + 1)]
        for n, c in freq.items():
            bucket[c].append(n)

        res = []
        for i in range(len(bucket) - 1, 0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res