from exam_prep.oop_exam_23_aug_21.project2.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library('Test')

    def test_correct_init(self):
        self.assertEqual('Test', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_with_wrong_data_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book(self):
        # If the author does not exist in the books_by_authors dict:
        self.library.books_by_authors = {}
        self.library.add_book('Author', 'Title')
        self.assertEqual({'Author': ['Title']}, self.library.books_by_authors)

        # If the author is existing in the books_by_authors dict, and we add new title:
        self.library.add_book('Author', 'Title2')
        self.assertEqual({'Author': ['Title', 'Title2']}, self.library.books_by_authors)

        # If both the author and the title exists:
        result = self.library.add_book('Author', 'Title')
        self.assertEqual(None, result)

    def test_add_reader(self):
        # if the reader does not exist in the reader's dict:
        self.library.add_reader('John')
        self.assertEqual({"John": []}, self.library.readers)

        # if the reader is already added:
        result = self.library.add_reader('John')
        self.assertEqual("John is already registered in the Test library.", result)

    def test_rent_book_if_the_reader_does_not_exist(self):
        result = self.library.rent_book('John', 'Author', 'Title')
        self.assertEqual("John is not registered in the Test Library.", result)

    def test_rent_book_if_the_author_does_not_exist(self):
        self.library.readers = {"John": []}
        result = self.library.rent_book('John', 'Author', 'Title')
        self.assertEqual("Test Library does not have any Author's books.", result)

    def test_rent_book_if_the_title_does_not_exist(self):
        self.library.readers = {"John": []}
        self.library.books_by_authors = {'Author': ["Title"]}
        result = self.library.rent_book('John', 'Author', 'Title2')
        self.assertEqual("""Test Library does not have Author's "Title2".""", result)

    def test_correctly_rent_a_book(self):
        self.library.readers = {"John": []}
        self.library.books_by_authors = {'Author': ["Title"]}
        self.library.rent_book('John', 'Author', 'Title')

        self.assertEqual({'John': [{"Author": 'Title'}]}, self.library.readers)
        self.assertEqual({'Author': []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()