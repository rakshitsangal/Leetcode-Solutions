class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def b(a):
            if a == n:
                sol.append(["".join(a) for a in c])
                return
            for x in range(n):
                if not e[x] and not d[a+x] and not rev[a-x]:
                    c[a][x] = 'Q'
                    e[x], d[a+x], rev[a-x] = True, True, True
                    b(a+1)
                    c[a][x] = '.'
                    e[x], d[a+x], rev[a-x] = False, False, False
        
        c= [['.' for j in range(n)] for j in range(n)]
        e, d, rev = [False]*n, [False]*(2*n), [False]*(2*n-1)
        sol = []
        b(0)
        return sol
