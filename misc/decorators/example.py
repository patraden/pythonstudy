def decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 10)
        print(func(*args, **kwargs))
        print("=" * 10)
    return wrapper


@decorator
def f(*args, **kwargs):
    return -1


if __name__ == "__main__":
    f()
