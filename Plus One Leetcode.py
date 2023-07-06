class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=[str(i) for i in digits]
        s=''.join(digits)
        a=int(s)+1
        l=list(str(a))
        l=[int(i) for i in l]
        return l
