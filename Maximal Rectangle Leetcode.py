class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        height = [0] * (m + 1)
        res = 0
        for row in matrix:
            for a in range(m):
                height[a] = height[a] + 1 if row[a] == '1' else 0
            stack = [-1]
            for a in range(m + 1):
                while height[a] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = a - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(a)
        return res
