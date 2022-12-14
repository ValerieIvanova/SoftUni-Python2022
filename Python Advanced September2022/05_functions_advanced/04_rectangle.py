def rectangle(length, width):
    if isinstance(length, int) and isinstance(width, int):
        def area():
            return f"Rectangle area: {length*width}"

        def perimeter():
            return f"Rectangle perimeter: {(length + width) * 2}"

        return area() + '\n' + perimeter()
    return 'Enter valid values!'


print(rectangle(2, 10))
print(rectangle('2', 10))