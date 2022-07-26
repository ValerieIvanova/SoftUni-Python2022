def valid_username(username_):

    def valid_length():
        if 3 <= len(username_) <= 16:
            return True
        return False

    def symbol_types():
        for char in username_:
            if not (char.isalnum() or char == '-' or char == '_'):
                return False
        return True

    def redundant():
        if ' ' in username_:
            return False
        return True

    if valid_length() and symbol_types() and redundant():
        return True
    return False


usernames = input().split(', ')
[print(f"{username}") for username in usernames if valid_username(username)]