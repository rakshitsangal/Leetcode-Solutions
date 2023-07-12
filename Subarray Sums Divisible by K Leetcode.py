class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict = defaultdict(int)
        dict[0] =1
        res = 0
        s = 0
        for n in nums:
            s +=n
            m = s%k
            res += dict[m]
            dict[m]+=1
        return res
