from listStack import Stack


def bracketsBalance(exp):
    s = Stack()
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
