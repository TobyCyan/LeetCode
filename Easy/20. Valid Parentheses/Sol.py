class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { '(' : ')', '{' : '}', '[' : ']'}

        for c in s:
            if c in pairs:
                # Opened bracket
                stack.append(c)
            else:
                # Closed bracket
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if pairs[top] != c:
                    return False
        
        # Stack must be empty
        return len(stack) == 0