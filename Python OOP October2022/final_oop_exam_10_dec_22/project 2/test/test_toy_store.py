from unittest import TestCase

from toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct_init(self):
        self.assertEqual(self.store.toy_shelf, {"A": None,
                                                "B": None,
                                                "C": None,
                                                "D": None,
                                                "E": None,
                                                "F": None,
                                                "G": None, })

    def test_add_toy_with_incorrect_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('H', 'Dora')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_existing_toy_raise_exception(self):
        self.store.toy_shelf = {"A": 'Dora',
                                "B": None,
                                "C": None,
                                "D": None,
                                "E": None,
                                "F": None,
                                "G": None, }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'Dora')
        self.assertEqual('Toy is already in shelf!', str(ex.exception))

    def test_add_toy_on_taken_shelf_raise_exception(self):
        self.store.toy_shelf = {"A": 'Dora',
                                "B": None,
                                "C": None,
                                "D": None,
                                "E": None,
                                "F": None,
                                "G": None, }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'Kitty')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_correctly(self):
        self.store.toy_shelf = {"A": 'Dora',
                                "B": None,
                                "C": None,
                                "D": None,
                                "E": None,
                                "F": None,
                                "G": None, }

        result = self.store.add_toy('B', 'Kitty')
        self.assertEqual("Toy:Kitty placed successfully!", result)
        self.assertEqual({"A": 'Dora',
                          "B": 'Kitty',
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None, }, self.store.toy_shelf)

    def test_remove_toy_with_non_existing_shelf_raise_exception(self):
        self.store.toy_shelf = {"A": 'Dora',
                                "B": None,
                                "C": None,
                                "D": None,
                                "E": None,
                                "F": None,
                                "G": None, }
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('X', 'Dora')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_non_existing_toy_raise_exception(self):
        self.store.toy_shelf = {"A": 'Dora',
                                "B": None,
                                "C": None,
                                "D": None,
                                "E": None,
                                "F": None,
                                "G": None, }

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', 'Kitty')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_correctly(self):
        self.store.toy_shelf = {"A": 'Dora',
                                "B": 'Kitty',
                                "C": None,
                                "D": None,
                                "E": None,
                                "F": None,
                                "G": None, }

        result = self.store.remove_toy('A', 'Dora')
        self.assertEqual("Remove toy:Dora successfully!", result)
        self.assertEqual({"A": None,
                          "B": 'Kitty',
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None, }, self.store.toy_shelf)
