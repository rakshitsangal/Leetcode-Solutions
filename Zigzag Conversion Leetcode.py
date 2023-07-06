class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        c=(2*numRows)-2
        ans=""
        for i in range(numRows):
            j=0
            while i+j<len(s):   
                ans+=s[j+i]
                sec=(j-i)+c
                if i!=0 and i!=numRows-1 and sec<len(s):
                    ans+=s[sec]
                j+=c
        return ans
