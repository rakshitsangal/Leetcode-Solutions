class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List = []
        for a in operations:
            if a == "D":
               stack.append(int(stack[-1])*2)  
            elif a == "C":
                stack.pop()
            elif a == "+":
                stack.append(int(stack[-1] + stack[-2]))
            else:
                stack.append(int(a))
        return sum(stack)
