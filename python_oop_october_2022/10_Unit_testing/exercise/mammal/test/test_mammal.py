from unittest import TestCase, main
from mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('name', 'type', 'sound')

    def test_correct_initializing(self):
        self.assertEqual('name', self.mammal.name)
        self.assertEqual('type', self.mammal.type)
        self.assertEqual('sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_if_make_sound_correct_message(self):
        result = self.mammal.make_sound()
        self.assertEqual('name makes sound', result)

    def test_get_kingdom_returns_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_if_info_returns_correct_message(self):
        result = self.mammal.info()
        self.assertEqual("name is of type type", result)


if __name__ == '__main__':
    main()