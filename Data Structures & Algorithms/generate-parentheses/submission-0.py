class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # valid: ()
        # input: n=1
            # ()
        # input: n=2
            # (()), ()()
        # input: n=3
            # ()()(), (())(), ()(()), ((()))
        # ( -> if n>0, choice: to close or to open another (, if n=0, can only close
            # if close: check if n>0, open again
            # if open: same choice: to close ot open again
        # time: O(n)
        # space: O(n)

        ret = []
        def dfs(n, sequence, open):
            if n == 0:
                while open:
                    sequence += ")"
                    open -= 1
                ret.append(sequence)
                return 
            if not sequence:
                dfs(n-1, sequence+"(", open+1)
            else:
                dfs(n-1, sequence+"(", open+1)
                if open:
                    dfs(n, sequence+")", open-1)
        dfs(n, "", 0)
        return ret