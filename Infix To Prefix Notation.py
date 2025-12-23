# function to return precedence of operators
def precedence(c):
    if c == '^':
        return 3
    elif c in ('*', '/'):
        return 2
    elif c in ('+', '-'):
        return 1
    else:
        return -1

# function to check if operator is right-associative
def isRightAssociative(c):
    return c == '^'

# function to check if a character is an operator
def isOperator(c):
    return c in "+-*/^"

# function to convert infix expression to prefix
def infixToPrefix(s):
    st = []
    result = []

    # scan from right to left
    for c in reversed(s):
        if c.isalnum():
            result.append(c)
        elif c == ')':
            st.append(c)
        elif c == '(':
            while st and st[-1] != ')':
                result.append(st.pop())
            if st:
                st.pop()  # remove ')'
        elif isOperator(c):
            while (st and isOperator(st[-1]) and
                  (precedence(st[-1]) > precedence(c) or
                  (precedence(st[-1]) == precedence(c) and isRightAssociative(c)))):
                result.append(st.pop())
            st.append(c)

    # pop remaining operators
    while st:
        result.append(st.pop())

    # reverse at the end to get correct prefix
    return ''.join(reversed(result))

if __name__ == "__main__":
    s = "a*(b+c)/d"
    print(infixToPrefix(s))