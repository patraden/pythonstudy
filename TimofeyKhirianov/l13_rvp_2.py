from TimofeyKhirianov import stack


def rvp_2(s: str):
    """
    converts postfix expression to infix
    >>> rvp_2("9 5 3 + 2 4 ^ - +")
    '9+5+3-2^4'
    >>> rvp_2("2 3 11 + 5 -*")
    '2*(3+11-5)'
    >>> rvp_2("3 11 + 5 -")
    '3+11-5'
    >>> rvp_2("3 11 5 + -")
    '3-(11+5)'
    >>> rvp_2("3 11 +")
    '3+11'
    >>> rvp_2("3 -11 +")
    '3+(-11)'
    >>> rvp_2("-3-11--12-")
    '-3-(-11)-(-12)'
    >>> rvp_2("5 2 3 ^ +")
    '5+2^3'
    >>> rvp_2("3 2 * 11 -")
    '3*2-11'
    >>> rvp_2("2 1 12 3 /-+")
    '2+1-12/3'
    >>> rvp_2("6 3 - 2 ^ 11 -")
    '(6-3)^2-11'
    >>> rvp_2("6 3 2 ^ - 11 -")
    '6-3^2-11'
    >>> rvp_2("162 2 1 + 4 ^ /")
    '162/(2+1)^4'
    >>> rvp_2("162 2 1 + -4 -9 - ^ /")
    '162/(2+1)^(-4-(-9))'
    >>> rvp_2("4 3 4 + + 4 5 6 + + * 11 12 + /")
    '(4+3+4)*(4+5+6)/(11+12)'
    >>> rvp_2("162 2 1 & 4 ^ /")
    >>> rvp_2("12/323/adhaksjdhasjdh")
    Traceback (most recent call last):
    IndexError: pop from empty list
    >>> rvp_2("")
    Traceback (most recent call last):
    IndexError: list index out of range
    """
    operators = stack_class.Stack()
    operands = stack_class.Stack()
    number = ''
    for i in range(len(s)):
        if s[i].isspace():
            continue
        elif s[i].isdigit():
            number += s[i]
            if not (s[i + 1].isdigit()):  # last character cannot be digital no 'i' condition is required
                if float(number) < 0:
                    operands.push(number)
                    operators.push('@')  # special operator mark for negative numbers (not expressions)
                else:
                    operands.push(number)
                    operators.push('#')  # special operator mark for positive numbers (not expressions)
                number = ''
        elif s[i] == '-' and i < (len(s) - 1) and s[i + 1].isdigit():
            number = s[i]
            continue
        else:  # s[i] in '-+/*^'
            operand1 = operands.pop()
            operand2 = operands.pop()
            operator1 = operators.pop()
            operator2 = operators.pop()
            if s[i] == '-':
                if operator1 in '@-+':
                    result = operand2 + '-' + '(' + operand1 + ')'
                else:
                    result = operand2 + '-' + operand1
            elif s[i] == '+':
                if operator1 == '@':
                    result = operand2 + s[i] + '(' + operand1 + ')'
                else:
                    result = operand2 + s[i] + operand1
            elif s[i] == '*':
                if operator2 in '^*#' and operator1 not in '^*#':
                    result = operand2 + s[i] + '(' + operand1 + ')'
                elif operator1 in '^*#' and operator2 not in '^*#':
                    result = '(' + operand2 + ')' + s[i] + operand1
                elif operator1 in '@-+/' and operator2 in '@-+/':
                    result = '(' + operand2 + ')' + s[i] + '(' + operand1 + ')'
                else:
                    result = operand2 + s[i] + operand1
            elif s[i] == '/':
                if operator2 in '#^*' and operator1 not in '#^*':
                    result = operand2 + s[i] + '(' + operand1 + ')'
                elif operator1 in '#^*' and operator2 not in '#^*':
                    result = '(' + operand2 + ')' + s[i] + operand1
                elif operator1 in '-+/@' and operator2 in '-+/@':
                    result = '(' + operand2 + ')' + s[i] + '(' + operand1 + ')'
                else:
                    result = operand2 + s[i] + operand1
            elif s[i] == '^':
                if operator2 in '#' and operator1 in '#':
                    result = operand2 + s[i] + operand1
                elif operator1 in '#' and operator2 not in '#':
                    result = '(' + operand2 + ')' + s[i] + operand1
                elif operator2 in '#' and operator1 not in '#':
                    result = operand2 + s[i] + '(' + operand1 + ')'
                else:
                    result = '(' + operand2 + ')' + s[i] + '(' + operand1 + ')'
            else:
                return
            operands.push(result)
            operators.push(s[i])
    return operands.top()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
