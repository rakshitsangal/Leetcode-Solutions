class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        p, q, r, t = abs(dividend), abs(divisor), 0, 1
        while p >= q or t > 1:
            if p >= q: r += t; p -= q; t += t; q += q
            else: t >>= 1; q >>= 1
        return min((-r, r)[dividend ^ divisor >= 0], (1 << 31) - 1)
