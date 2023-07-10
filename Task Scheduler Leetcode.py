class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        ret = Counter(tasks)
        maxfreq = max(ret.values())
        count = 0
        for val in ret.values():
			if val == maxfreq:
				count += 1
        return max(maxfreq+ (maxfreq-1)*n + count -1,len(tasks))
