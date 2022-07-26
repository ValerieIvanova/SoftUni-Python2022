def password_validator(password):
    valid = True
    if len(password) < 6 or len(password) > 10:
        print('Password must be between 6 and 10 characters')
        valid = False

    if not password.isalnum():
        print('Password must consist only of letters and digits')
        valid = False

    digits_counter = 0
    for char in password:
        if char.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print('Password must have at least 2 digits')
        valid = False
    return valid


current_password = input()
is_valid = password_validator(current_password)
if is_valid:
    print('Password is valid')


# def length_is_valid(some_string):
#     if 6 <= len(some_string) <= 10:
#         return True
#     print('Password must be between 6 and 10 characters')
#     return False
#
#
# def symbols_are_valid(some_string):
#     if some_string.isalnum():
#         return True
#     print('Password must consist only of letters and digits')
#     return False
#
#
# def have_two_digits(some_string):
#     digits_counter = 0
#     for char in some_string:
#         if char.isdigit():
#             digits_counter += 1
#     if digits_counter >= 2:
#         return True
#     print('Password must have at least 2 digits')
#     return False
#
#
# password = input()
# validation = [length_is_valid(password), symbols_are_valid(password), have_two_digits(password)]
# if all(validation):
#     print('Password is valid')