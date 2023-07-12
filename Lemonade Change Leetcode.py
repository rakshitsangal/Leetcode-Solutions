class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count5=0
        count10=0
        for ii in bills:
            if ii==5:
                count5+=1
            elif ii==10:
                if count5==0:
                    return False
                count10+=1
                count5-=1
            else:
                if count5>=1 and count10>=1:
                    count10-=1
                    count5-=1
                elif count5>=3:
                    count5-=3
                else:
                    return False
        return True
