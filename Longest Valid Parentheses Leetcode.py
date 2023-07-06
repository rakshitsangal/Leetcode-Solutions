class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        a=[[s[0],1,0]]
        for i in range(1,len(s)):
            
            if s[i] == "(" :
                if a[-1][0]==")":
                    a.append(["(",1,0])
                else:
                    if a[-1][2]>0:
                        a.append(["(",1,0])
                    else:
                        a[-1][1]+=1
            
            else:
                if a[-1][0]=="(" and a[-1][1]>0:
                    a[-1][1]-=1
                    a[-1][2]+=1
                    
                    if len(a)>=2 and a[-2][0]=="(" and a[-1][1]==0:
                        a[-2][2]+=a[-1][2]
                        a.pop()
                elif a[-1][0]=="(":
                    a.append([")",1,0])
        ans=0
        for i in a:
            if i[2]>ans:
                ans=i[2]
        return ans*2
