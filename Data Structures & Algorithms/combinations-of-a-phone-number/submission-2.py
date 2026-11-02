class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        ret = []
        phone = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def backtrack(comb, index):
            if index == len(digits):
                ret.append(comb)
                return 

            for l in phone[int(digits[index])]:
                backtrack(comb + l, index + 1)


        backtrack("", 0)
        return ret