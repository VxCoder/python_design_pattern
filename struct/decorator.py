import functools


def memoize(fn):
    known = {}

    @functools.wraps(fn)
    def wraps(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return wraps


@memoize
def nsum(n):
    """返回前n个数字的和"""
    assert n >= 0, "n must be <= 0"
    return 0 if n == 0 else n + nsum(n - 1)


@memoize
def fibonacci(n):
    """返回斐波那契数列的第n个数"""
    assert n >= 0, "n must be >= 0"
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    from timeit import Timer

    measure = [
        {"exec": "fibonacci(100)", "import": "fibonacci", "func": fibonacci},
        {"exec": "nsum(200)", "import": "nsum", "func": nsum},
    ]

    for m in measure:
        t = Timer(f"{m['exec']}", f'from __main__ import {m["import"]}')
        print(
            f"name: {m['func'].__name__}, doc: {m['func'].__doc__}, executing: {m['exec']}, time: {t.timeit()}"
        )
