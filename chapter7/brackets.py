from .stack.listStack import ListStack


def bracketsBalance(exp):
    s = ListStack()
    for ch in exp:
        if ch in ('{', '[', '('):
            s.push(ch)
        elif ch in ('}', ']', ')'):
            if s.is_empty():
                return False
            chFromStack = s.pop()
            if (ch == '}' and chFromStack != '{') or \
                (ch == ']' and chFromStack != '[') or \
                    (ch == ')' and chFromStack != '('):
                return False
    return s.is_empty()
