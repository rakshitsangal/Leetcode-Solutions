class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ranks= [[] for _ in range(len(nums) + 1)]
        c = Counter(nums)
        for key, val in c.items():
            ranks[val].append(key)
        return list(chain(*ranks))[len(c) - k:]
