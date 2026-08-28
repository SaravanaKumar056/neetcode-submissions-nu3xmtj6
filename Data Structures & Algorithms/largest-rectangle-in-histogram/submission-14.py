class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_res = 0
        for i, n in enumerate(heights):
            current = i
            while stack and n <= stack[-1][1]:
                index, num = stack.pop()
                max_res = max(max_res, (i - index) * num)
                current = index
            stack.append((current, n))
        
        n = len(heights)
        for i, h in stack:
            max_res = max(max_res, (n - i) * h)
        return max_res