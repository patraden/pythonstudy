def decorator_params(a=10, b=30):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("=" * a)
            print(func(*args, **kwargs))
            print("=" * b)
        return wrapper
    return decorator


@decorator_params(a=100, b=40)
def f(*args, **kwargs):
    return -1


if __name__ == "__main__":
    f()
