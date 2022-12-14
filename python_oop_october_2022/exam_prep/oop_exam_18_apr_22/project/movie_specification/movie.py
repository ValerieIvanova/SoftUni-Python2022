from abc import ABC, abstractmethod

from exam_prep.oop_exam_18_apr_22.project.user import User


class Movie(ABC):

    MIN_AGE = None

    @abstractmethod
    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value or value.isspace():
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.MIN_AGE:
            raise ValueError(f"{self.__class__.__name__} movies must be restricted "
                             f"for audience under {self.MIN_AGE} years!")
        self.__age_restriction = value

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"