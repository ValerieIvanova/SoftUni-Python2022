def even_parameters(func_ref):
    def wrapper(*args):
        for num in args:
            if isinstance(num, int):
                if num % 2 == 0:
                    continue

            return "Please use only even numbers!"
        result = func_ref(*args)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
