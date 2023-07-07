# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution:
    def guessNumber(self, n: int) -> int:

        l, r= 1, n                         
        while r >= l: 
            m = (l + r)//2
            query =  guess(m)
            if query ==  1: l = m+1        
            elif query == -1: r = m  
            else: return m
