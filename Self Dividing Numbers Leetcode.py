class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l=[]
        for i in range(left,right+1):
            fl,a=0,i
            if '0' in str(i):
                fl=1
            else:
                while a!=0:
                    if i%(a%10)!=0:
                        fl=1
                        break
                    a=a//10
            if fl==0:
                l.append(i)
        return l
