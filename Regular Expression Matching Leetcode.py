class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i>=len(s) and j>=len(p):
                return True
            if i<= len(s) and j>= len(p):
                return False
            match  =  i< len(s) and ((s[i] == p[j]) or (p[j] == '.'))
            
            if j < len(p)-1 and  p[j+1] == '*':
                dp[(i,j)] = ( dfs(i,j+2) # dont use *  
                    or (match and dfs(i+1,j)) )
                return dp[(i,j)]
            if match:
                dp[(i,j)] = dfs(i+1,j+1) 
                return dp[(i,j)]
        
        return dfs(0,0)
