from exam_prep.oop_exam_10_apr_22.project2.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Test', 1992, 5.5)

    def test_correct_init(self):
        self.assertEqual('Test', self.movie.name)
        self.assertEqual(1992, self.movie.year)
        self.assertEqual(5.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_with_incorrect_data_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.incorrect_movie = Movie('', 1992, 5.5)
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_with_wrong_data_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.incorrect_movie = Movie('Test', 1886, 5.5)
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor(self):
        self.movie.actors = ['Actor1']
        self.movie.add_actor('Actor2')
        self.assertEqual(['Actor1', 'Actor2'], self.movie.actors)

        result = self.movie.add_actor('Actor1')
        self.assertEqual("Actor1 is already added in the list of actors!", result)

    def test_greater_than_method(self):
        self.second_movie = Movie('Test2', 1999, 5.9)
        self.assertEqual(self.movie > self.second_movie, '"Test2" is better than "Test"')
        self.second_movie = Movie('Test2', 1999, 3.5)
        self.assertEqual(self.movie > self.second_movie, '"Test" is better than "Test2"')

    def test_repr_method(self):
        result = 'Name: Test\nYear of Release: 1992\nRating: 5.50\nCast: '
        self.assertEqual(repr(self.movie), result)
        self.movie.actors = ['Actor1', 'Actor2']
        result2 = 'Name: Test\nYear of Release: 1992\nRating: 5.50\nCast: Actor1, Actor2'
        self.assertEqual(repr(self.movie), result2)


if __name__ == '__main__':
    main()