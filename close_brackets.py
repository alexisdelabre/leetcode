def isValid(s: str) -> bool:
    open = ['[', '(', '{']
    close = [']', ')', '}']

    stack = []

    for char in s:
        if char in open:
            stack.append(char)
        elif char in close:
            if len(stack) == 0:
                return False
            indexChar = close.index(char)
            if stack[-1] == open[indexChar]:
                stack.pop()
            else:
                return False
    return True if stack == [] else False

isValid("([])[]{}")