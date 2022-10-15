def gen_bin(m: int, prefix=""):
    if m == 0:
        print(prefix)
        return
    gen_bin(m - 1, prefix + "0")
    gen_bin(m - 1, prefix + "1")


def generate_numbers(n: int, m: int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
    в n-ричной системе счисления (n<=10)
    длины m """
    if m == 0:
        print(*prefix, sep="")
        return
    prefix = prefix or []
    for digit in range(n):  # рекурентный вызов в цикле
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


def find(number, a):
    """ Ищет number в A и возвращает True, если такой есть
    False, если такого нет """
    for x in a:
        if number == x:
            return True
    return False


def generate_permutations(n: int, m: int = -1, prefix=None):
    """ Генерация перестановок n чисел в m позициях,
    с префиксом prefix """
    m = n if m == -1 else m  # по умолчанию n чисел в n позициях
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep="")
        return
    for number in range(1, n + 1):
        if find(number, prefix):
            continue  # пропустит шаг цикла
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


if __name__ == "__main__":
    generate_permutations(5, 5)
#    generate_numbers(3,3)
#    gen_bin(3)
