from collections import deque


class vowels:
    ALL_VOWELS = 'AEIUYOaeiuyo'

    def __init__(self, string):
        self.string = string
        self.vowels_in_string = deque([el for el in self.string if el in vowels.ALL_VOWELS])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_in_string:
            raise StopIteration
        return self.vowels_in_string.popleft()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
