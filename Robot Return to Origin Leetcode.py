class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l,r,u,d=0,0,0,0
        for i in moves:
            if i=='L':
                l+=1
            elif i=='D':
                d+=1
            elif i=='U':
                u+=1
            elif i=='R':
                r+=1
        if d-u==0 and r-l==0:
            return True
        return False
