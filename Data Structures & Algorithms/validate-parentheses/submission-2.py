class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in pairs:
                #c is a closing bracket
                if stack == []:
                    return False
                if stack[-1] == pairs[c]:
                    stack.pop()
                elif stack[-1] != pairs[c]:
                    return False
            else:
                #c is an opening bracket
                stack.append(c)
                
        return stack == []

        