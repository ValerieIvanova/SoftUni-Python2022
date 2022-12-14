def logged(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return f"you called {func_ref.__name__}({', '.join(str(arg) for arg in args)})\n" \
               f"it returned {result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
