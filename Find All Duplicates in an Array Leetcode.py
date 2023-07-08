class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
	    c = collections.Counter(nums)
	    res = []
	    for k, v in c.items():
		    if v == 2:
			    res.append(k)
	    return res
