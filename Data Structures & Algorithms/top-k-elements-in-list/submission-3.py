class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freaq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for num, cnt in count.items():
            freaq[cnt].append(num)
        
        res = []
        for i in range(len(freaq)-1, 0, -1):
            for n in freaq[i]:
                res.append(n)
                if len(res) == k:
                    return res