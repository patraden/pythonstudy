import l13_stack as A_stack


def is_brackets_sequence_correct(s: str):
    """
    проверяет корректность скобочной последовательности
    из круглых и квадратных скобок () []
    >>> is_brackets_sequence_correct("(([()]))[]")
    True
    >>> is_brackets_sequence_correct("(])]")
    False
    >>> is_brackets_sequence_correct("(")
    False
    >>> is_brackets_sequence_correct("]")
    False
    """
    for bracket in s:
        if bracket not in "()[]":
            continue
        if bracket in "([":
            A_stack.push(bracket)
        else:  # bracket in ")]"
            assert bracket in ")]", "Ожидалась закрывающая скобка!" + str(bracket)
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            assert left in "([", "Ожидалась открывающая скобка!" + str(left)
            if left == "(":
                right = ")"
            else:
                right = "]"
            if right != bracket:
                return False
    return A_stack.is_empty()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
