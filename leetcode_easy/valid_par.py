s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"
s5 = "([)]"


def isValid(s):
    """
    :type s: str
    :rtype: bool
    1. opened must be closed
    2. correct order
    3. closed must have been opened
    stack -> lifo
    """
    par = {")": "(", "}": "{", "]": "["}
    stack = []

    for st in s:
        if st in par:
            if not stack or par[st] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(st)
    return not stack
