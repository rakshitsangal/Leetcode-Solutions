class Solution:
    dic={ 1000:'M',  500:'D',  100:'C',  50:'L',  10:'X',  5:'V',  1:'I'}
    def intToRoman(self, num: int) -> str:
        ans=""
        for x,y in self.dic.items():
            if num==0:
                break
            if num>=x:
                ans+=y*(num//x)
                num%=x
            a=10**(ceil(log10(x))-1)
            if x <= num+a:
                ans+=self.dic[a]+y
                num-=x-a
        return ans
