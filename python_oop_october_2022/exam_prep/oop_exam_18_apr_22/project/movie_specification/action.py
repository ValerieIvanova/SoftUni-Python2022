from exam_prep.oop_exam_18_apr_22.project.movie_specification.movie import Movie
from exam_prep.oop_exam_18_apr_22.project.user import User


class Action(Movie):
    MIN_AGE = 12

    def __init__(self, title, year, owner: User, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)