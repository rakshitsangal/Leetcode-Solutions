class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums
        else:
            a=b=nums[0]
            out=[]
            for i in nums[1:]:
                if b == i-1:
                    b = i
                else:
                    if a!=b: out.append(str(a)+"->"+str(b))
                    else: out.append(str(a))
                    a=b=i
            if a!=b: out.append(str(a)+"->"+str(b))
            else: out.append(str(a))
            return out
