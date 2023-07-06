class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in s:
            if i in ['(','{','[']:
                l.append(i)
            elif i==')' and len(l)!=0 and l[-1]=='(':
                l.pop()
            elif i=='}' and len(l)!=0 and l[-1]=='{':
                l.pop()
            elif i==']' and len(l)!=0 and l[-1]=='[':
                l.pop()
            else:
                return False
        return l==[]
