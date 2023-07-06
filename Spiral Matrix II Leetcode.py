class Solution:
    def generateMatrix(self, n):
        A = [[n*n]]
        while A[0][0] > 1:
            A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
        return A * (n>0)
