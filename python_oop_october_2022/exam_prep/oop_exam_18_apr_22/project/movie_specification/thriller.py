from exam_prep.oop_exam_18_apr_22.project.movie_specification.movie import Movie
from exam_prep.oop_exam_18_apr_22.project.user import User


class Thriller(Movie):
    MIN_AGE = 16

    def __init__(self, title, year, owner: User, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)
