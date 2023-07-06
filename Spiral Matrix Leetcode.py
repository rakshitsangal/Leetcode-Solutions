class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiralOrder = []
        n, m = len(matrix), len(matrix[0])
        r, c, dr, dc = 0, 0, 0, 1
        while len(spiralOrder) < n * m:
            spiralOrder.append(matrix[r][c])
            matrix[r][c] = float('inf')
            if not(0 <= r + dr < n) or not(0 <= c + dc < m) or matrix[r + dr][c + dc] == float('inf'):
                dr, dc = dc, -dr
            r += dr
            c += dc
        return spiralOrder
