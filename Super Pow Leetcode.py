class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        s=0
        for i in b:
            if i==0:
                s*=10
            else:
                s=s*10+i
        return (pow(a,s,1337))
        
