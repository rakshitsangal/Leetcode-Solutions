class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n,a= 1, 0
        for k, c in enumerate(chars + ['&&&&&&']): 
            if k == 0 or c != chars[k - 1]: 
                if n > 1:   
                    for d in str(n): 
                        chars[a] = d
                        a += 1
                if a < len(chars): chars[a] = c   
                a += 1   
                n = 1  
            else: 
                n += 1 
        return a - 1
