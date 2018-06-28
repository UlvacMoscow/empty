from datetime import datetime


# декораторы

def timeit(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@timeit('name')
def one(n):
    lst = []
    for i in range(n):
        if i % 2 == 0:
            lst.append(i)
        return lst


@timeit('name')
def two(m):
    lst = [x for x in range(m) if x % 2 == 0]
    return lst


li = timeit('name')(one)(10)

