class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        nums = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        def backTrack(combination, next_digits):
            if not next_digits:
                ans.append(combination)
                return
            for letter in nums[next_digits[0]]:
                backTrack(combination + letter, next_digits[1:])        
        backTrack("", digits)
        return ans
