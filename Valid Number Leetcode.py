class Solution:
    def isNumber(self,s:str)->bool:
        try:
            float(s)
        except:
            return False
        return "inf" not in s.lower()               
