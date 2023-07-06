class Solution(object):
    def groupAnagrams(self, strs):
        a = {}
        for i in strs:
            sk = "".join(sorted(i))    
            if sk in a:
                a[sk].append(i)
            else:
                a[sk] = [i]
        return a.values()             
