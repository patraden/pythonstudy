def gen_bin(m: int, prefix=""):
    """
    Generates all valid numbers (with leading zeroes) of length m in binary numeric system.
    """
    if m == 0:
        print(prefix)
        return
    gen_bin(m - 1, prefix + "0")
    gen_bin(m - 1, prefix + "1")


def generate_numbers(n: int, m: int, prefix=None):
    """
    Generates all valid numbers (with leading zeroes) of length m in n-base numeric system.
    n <= 10.
    """
    assert (n <= 10)
    if m == 0:
        print(*prefix, sep="")
        return
    # IMPORTANT! if we put this a default arg value then python will use this [] for all calls to this function
    prefix = prefix or []
    for digit in range(n):  # recursive call in a loop
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


def find(number, a: list):
    """ Searches number in array/list. """
    for x in a:
        if number == x:
            return True
    return False


def generate_permutations(n: int, m: int = -1, prefix=None):
    """ Generate permutations of n numbers in m positions with prefix. """
    m = n if m == -1 else m  # by default n numbers in n positions
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep="")
        return
    for number in range(1, n + 1):
        if find(number, prefix):
            continue  # skip this loop iteration
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


if __name__ == "__main__":
    generate_permutations(5)
    # generate_numbers(2, 5)
    # gen_bin(3)
