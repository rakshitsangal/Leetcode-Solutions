class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        cm = len(mat[0])
        if r*c != len(mat)*cm:
            return mat
        
        out = [[] for i in range(r)]
        for i in range(r*c):
            out[i//c].append(mat[i//cm][i%cm])
        return out
