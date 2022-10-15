def is_simple_number(x: int) -> bool:
    """ Validates if integer number is simple. """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def factorize_number(x: int):
    """ Factorizes integer number. """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1


if __name__ == "__main__":
    factorize_number(999)
    print(is_simple_number(19))
