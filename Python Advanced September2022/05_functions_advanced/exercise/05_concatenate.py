def concatenate(*args, **kwargs):
    concatenated_strings = ''.join(args)
    for key, value in kwargs.items():
        concatenated_strings = concatenated_strings.replace(key, value)
    return concatenated_strings


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))