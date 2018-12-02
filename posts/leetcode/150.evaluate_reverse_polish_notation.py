def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for t in tokens:
        if t in '+-*/':
            right = stack.pop()
            left = stack.pop()
            res = 0
            if t == '+':
                res = left + right
            elif t == '-':
                res = left - right
            elif t == '*':
                res = left * right
            elif t == '/':
                res = left / right
            stack.append(res)
        else:
            stack.append(eval(t))
        print(stack)
    return stack.pop()
