class Solution:
    def generateParenthesis(self, n:int):

        res, stack = [],[]

        def backtracker(op, cp):

            if op == cp == n:
                res.append("".join(stack))
                return

            if op < n:
                stack.append("(")
                backtracker(op+1, cp)
                stack.pop()

            if cp<op:
                stack.append(")")
                backtracker(op, cp+1)
                stack.pop()

        backtracker(0,0)
        return res
