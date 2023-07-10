class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        li=[0]+flowerbed+[0]
        c=0
        for ii in range(0,len(li)):
            if li[ii:ii+3]==[0,0,0]:
                c+=1
                li[ii+1]=1
        return c>=n        
