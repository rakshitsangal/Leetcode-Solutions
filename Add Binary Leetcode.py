class Solution(object):
    def addBinary(self, a, b):
        res,c= "",0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or c!= 0:
            sum = c
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            res = str(sum % 2) + res
            c=sum // 2
        return res
